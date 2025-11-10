import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Alumnos')

    body = json.loads(event['body'])
    alumno_id = body['alumno_id']

    response = table.update_item(
        Key={'alumno_id': alumno_id},
        UpdateExpression="set nombre=:n, edad=:e, carrera=:c",
        ExpressionAttributeValues={
            ':n': body['nombre'],
            ':e': body['edad'],
            ':c': body['carrera']
        },
        ReturnValues="UPDATED_NEW"
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'mensaje': 'Alumno modificado', 'data': response['Attributes']})
    }
