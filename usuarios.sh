#!/bin/bash
echo "Configurando usuarios y permisos"
sudo useradd devops_user
sudo groupadd devops_group
sudo usermod -aG devops_group devops_user
#Permisos para ec2 user
sudo chown -R ec2-user:ec2-user ~/environment
echo "Usuarios configurados correctamente."
