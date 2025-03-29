import boto3
import os
import sys

s3 = boto3.client('s3')
BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "bucket-juan-images")

def upload_to_s3(file_path, bucket_name):
    if not os.path.exists(file_path):
        print(f"❌ Archivo no encontrado: {file_path}")
        return

    file_name = os.path.basename(file_path)
    s3.upload_file(file_path, bucket_name, file_name)
    print(f"✅ {file_name} subido correctamente a {bucket_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Debes especificar la imagen a subir. Uso: python upload.py /ruta/imagen.jpg")
        sys.exit(1)

    IMAGE_PATH = sys.argv[1]
    upload_to_s3(IMAGE_PATH, BUCKET_NAME)
