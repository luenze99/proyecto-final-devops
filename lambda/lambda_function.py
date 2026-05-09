import json
import random

def lambda_handler(event, context):
    mensajes = [
        "Despliegue exitoso en AWS",
        "Microservicio DevOps activo",
        "Arquitectura serverless configurada",
        "Pipeline CI/CD funcionando",
        "Monitorización activa con CloudWatch"
    ]
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensaje': random.choice(mensajes),
            'servicio': 'microservicio-devops'
        })
    }