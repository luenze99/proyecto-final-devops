import boto3
import time

#Configuración
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
TABLE_NAME = 'devops-tabla'

#Crear tabla
try:
    table = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
        BillingMode='PAY_PER_REQUEST'
    )
    print(f"Creando tabla {TABLE_NAME}...")
    table.wait_until_exists()
    print("Tabla creada con éxito")
except dynamodb.meta.client.exceptions.ResourceInUseException:
    print("La tabla ya existe")
    table = dynamodb.Table(TABLE_NAME)

#Insertar un registro
table.put_item(
    Item={
        'id': '1',
        'nombre': 'Luis Segura',
        'status': 'inicial'
    }
)
print("Registro insertado")

#Modificar el status
table.update_item(
    Key={'id': '1'},
    UpdateExpression="SET #st = :new_status",
    ExpressionAttributeNames={'#st': 'status'},
    ExpressionAttributeValues={':new_status': 'completado'}
)
print("Registro actualizado (status cambiado a 'completado')")

#Eliminar el registro
table.delete_item(Key={'id': '1'})
print("Registro eliminado exitosamente")