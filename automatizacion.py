import boto3
from datetime import datetime, timedelta

#Obtención de métricas de CloudWatch
def obtener_metricas_cpu(instance_id):
    cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
    ahora = datetime.utcnow()
    hace_24h = ahora - timedelta(days=1)
    
    metrica = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=hace_24h,
        EndTime=ahora,
        Period=86400,
        Statistics=['Average']
    )
    return f"{metrica['Datapoints'][0]['Average']:.2f}%" if metrica['Datapoints'] else "Sin datos"
    
def listar_recursos():
    #Conexión a los servicios
    ec2 = boto3.client('ec2', region_name='us-east-1')
    s3 = boto3.client('s3')
    asg = boto3.client('autoscaling', region_name='us-east-1')
    
    #Listar Instancias EC2
    print("--- Listado de Instancias EC2 ---")
    instancias = ec2.describe_instances()
    for reserva in instancias['Reservations']:
        for instancia in reserva['Instances']:
            id_instancia = instancia['InstanceId']
            tipo = instancia['InstanceType']
            estado = instancia['State']['Name']
            cpu = obtener_metricas_cpu(id_instancia) if estado == 'running' else "N/A"
            print(f"ID: {id_instancia} | Tipo: {tipo} | Estado: {estado} | CPU (24h): {cpu}")

    print("\n--- Listado de Buckets S3 ---")
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        print(f"Nombre: {bucket['Name']}")
        
    #Listar Buckets S3 y objetos
    print("\n--- BUCKETS S3 Y OBJETOS ---")
    for b in s3.list_buckets()['Buckets']:
        name = b['Name']
        print(f"Bucket: {name}")
        objs = s3.list_objects_v2(Bucket=name)
        if 'Contents' in objs:
            for obj in objs['Contents']: print(f"  └─ Objeto: {obj['Key']}")
        else: print("  └─ (Vacío)")
        
    #Consulta de grupos de Auto Scaling
    print("\n--- Grupos de AUTO SCALING ---")
    grupos = asg.describe_auto_scaling_groups()['AutoScalingGroups']
    if not grupos: print("No hay grupos de Auto Scaling configurados")
    for g in grupos:
        print(f"Nombre: {g['AutoScalingGroupName']}")
        print(f"   Capacidad: [Mín: {g['MinSize']} | Máx: {g['MaxSize']} | Deseada: {g['DesiredCapacity']}]")
    

if __name__ == "__main__":
    listar_recursos()
    
