import boto3
import os

# Configura el cliente S3
s3 = boto3.client('s3')

# Nombre del bucket
BUCKET_NAME = "tu-bucket-s3"

# Directorio donde están las imágenes dentro del contenedor
UPLOAD_FOLDER = "/app/photos"

# Subir archivos
for filename in os.listdir(UPLOAD_FOLDER):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.isfile(file_path):
        s3.upload_file(file_path, BUCKET_NAME, filename)
        print(f"Subido: {filename}")
