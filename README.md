Diprojek kali ini saya akan mendemonstrasikan cara membuat sebuah system event driven pipeline Aws tapi menggunakan Localstack karena saya tidak punya uang untuk sewa aws 
jadinya saya memutar otak mencari cara bagaimana saya bisa belajar aws tanpa mengeluarkan uang sepeserpun,localstack ini hanya mock api dari aws jadi untuk resouce aws asli 
sepeerti ec2 itu tidak bisa di buat dan bukan sebuah node asli dan postingan projek ini hanya berupa langkah awal atau step 1 dari sebuah projek yang cukup rumit menurut 
saya.Projek berikutnya mengganti semua resource yang tidak bisa digunakan seperti ec2 karena localstack hanya mock api dari aws jadinya tidak ada node asli,lalu 
eks,cloudwatch,dll.Semua resource yang tidak bisa berjalan seperti service aws asli akan diganti dengan tools opensource yang memiliki kegunaan yang sama seperti ec2 dengan 
KVM/QEMU,lalu observ tools dengan plg stack dan container orchestration eks dengan kubernetes asli,langsung saja masuk ke pembahasan.

![oihve](/asset/workflow-aws-1.png)

### Structure Folder

```
terraform-setup/
├── .terraform/
├── compute.tf
├── main.tf
├── prep-vm.tf
├── terraform.tfstate
├── terraform.tfstate.backup
├── s3.tf
├── sns.tf
├── sqs.tf
├── sqs-trigger-lambda.tf
├── iam-attachment-role.tf
├── iam-attachment-role-consumer.tf
├── lambda_function_consumer.py
├── lambda_function.py
├── lambda-permission.tf
├── lambda.tf
├── lambda-2.tf
├── cloud-watch.tf
├── cloud-watch-metrics.tf
├── dynamodb.tf
├── terraform.tfvars
```



### Tools
- **Wsl** : v0.2.1
- **Terraform** : v1.15.8
- **Localstack** : v2026.6.3
- **Docker** : v29.1.3
- **Python** : v3.12.3
- **Aws Cli** : v1.45.52
  
### Reasoning 
Kenapa saya mengerjakan projek ini terlebih dahulu?? karena ini merupakan alur pembelajaran jadinya saya bisa belajar service-service aws terlebih dahulu tidak langsung 
masuk ke projek yang sesungguhnya saya harus belajar daulu dari awal.
