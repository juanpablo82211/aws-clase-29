FROM amazonlinux:latest

RUN yum install -y python3 pip && pip3 install boto3

COPY upload.py /app/upload.py

CMD ["python3", "/app/upload.py"]