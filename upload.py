import boto3
import os

s3 = boto3.client('s3')

def upload_to_s3(file_path, bucket_name):
    file_name = os.path.basename(file_path)
    s3.upload_file(file_path, bucket_name, file_name)
    print(f"{file_name} subido a {bucket_name}")

# Ejemplo de uso
upload_to_s3("imagen.jpg", "bucket-juan-images")
