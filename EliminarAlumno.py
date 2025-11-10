import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Alumnos')

    alumno_id = event['pathParameters']['id']
    table.delete_item(Key={'alumno_id': alumno_id})

    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': f'Alumno {alumno_id} eliminado'})
    }
