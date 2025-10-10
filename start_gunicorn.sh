#!/bin/bash

export DB_NAME=$(aws ssm get-parameter --name "/django-short-url-generator/DB_NAME" --query "Parameter.Value" --output text --with-decryption)
export DB_USER=$(aws ssm get-parameter --name "/django-short-url-generator/DB_USER" --query "Parameter.Value" --output text --with-decryption)
export DB_PASSWORD=$(aws ssm get-parameter --name "/django-short-url-generator/DB_PASSWORD" --query "Parameter.Value" --output text --with-decryption)
export DB_HOST=$(aws ssm get-parameter --name "/django-short-url-generator/DB_HOST" --query "Parameter.Value" --output text --with-decryption)
export DB_PORT=$(aws ssm get-parameter --name "/django-short-url-generator/DB_PORT" --query "Parameter.Value" --output text --with-decryption)

cd /home/ubuntu/short-url-generator
source .venv/bin/activate
exec make run-production