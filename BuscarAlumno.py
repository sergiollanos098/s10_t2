import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Alumnos')

    alumno_id = event['pathParameters']['id']
    response = table.get_item(Key={'alumno_id': alumno_id})

    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'mensaje': 'Alumno no encontrado'})
        }
