import json
import time
import os
import urllib.request
import urllib.error
import boto3

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = "PipelineHistory"
table = dynamodb.Table(TABLE_NAME)

BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')


def send_telegram_alert(text):
    if not BOT_TOKEN or not CHAT_ID:
        print("TELEGRAM_BOT_TOKEN atau TELEGRAM_CHAT_ID belum diset, skip alert")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = json.dumps({
        "chat_id": CHAT_ID,
        "text": text
    }).encode('utf-8')

    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            print(f"Telegram alert terkirim, status: {response.status}")
    except urllib.error.HTTPError as e:
        print(f"Telegram API error: {e.code} - {e.read().decode('utf-8')}")
    except urllib.error.URLError as e:
        print(f"Gagal konek ke Telegram API: {str(e)}")


def lambda_handler(event, context):
    print(f"RAW EVENT: {json.dumps(event)}")

    for record in event['Records']:
        body = json.loads(record['body'])
        original_message = body.get('Message', 'Pesan tidak ditemukan')
        sns_message_id = body.get('MessageId', record.get('messageId', 'unknown'))

        print(f"Pesan diterima dari SQS: {original_message}")

        item = {
            'event_id': sns_message_id,
            'timestamp': int(time.time() * 1000),
            'message': original_message,
            'source': 'sqs-consumer-lambda',
            'status': 'processed',
        }

        try:
            table.put_item(Item=item)
            print(f"Berhasil ditulis ke DynamoDB: {item['event_id']}")
        except Exception as e:
            print(f"GAGAL nulis ke DynamoDB: {str(e)}")

            send_telegram_alert(f"GAGAL nulis history ke DynamoDB!\n{original_message}\nError: {str(e)}")
            raise


        send_telegram_alert(f" Pipeline event diproses:\n{original_message}")

    return {
        'statusCode': 200,
        'body': json.dumps('Pesan berhasil diproses, dicatat ke DynamoDB, dan alert terkirim')
    }
