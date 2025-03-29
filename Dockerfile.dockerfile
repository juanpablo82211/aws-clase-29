FROM python:3.9
RUN pip install boto3
COPY upload.py /app/upload.py
WORKDIR /app
CMD ["python", "upload.py"]
