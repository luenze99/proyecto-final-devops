import boto3
import os

#Configuración
s3 = boto3.client('s3')
BUCKET_NAME = 'bucket-proyecto-final-luis-588991582465'
FILE_NAME = 'archivo_prueba.txt'
S3_KEY = 'pruebas/' + FILE_NAME

#Crear el archivo de prueba local
with open(FILE_NAME, 'w') as f:
    f.write('Archivo de prueba para proyecto final')

#Subirlo al bucket S3 en la carpeta "pruebas/"
try:
    s3.upload_file(FILE_NAME, BUCKET_NAME, S3_KEY)
    print(f"Archivo {FILE_NAME} subido exitosamente a {BUCKET_NAME}/{S3_KEY}")
except Exception as e:
    print(f"Error al subir: {e}")

#Listar objetos del bucket
print("\n--- Listado de objetos en el bucket ---")
response = s3.list_objects_v2(Bucket=BUCKET_NAME)

if 'Contents' in response:
    for obj in response['Contents']:
        print(f"Nombre: {obj['Key']} | Tamaño: {obj['Size']} bytes | Modificado: {obj['LastModified']}")
else:
    print("El bucket está vacío")