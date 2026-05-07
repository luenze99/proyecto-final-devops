#!/bin/bash
echo "Instalando dependencias de Python y Boto3..."
sudo yum update -y
sudo yum install -y python3-pip
pip install boto3 flask==2.3.3
echo "Instalación completada."
