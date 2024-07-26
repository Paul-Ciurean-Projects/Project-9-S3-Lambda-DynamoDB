import boto3
import csv
import os

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME'] # Remember to create an ENV for "TABLE_NAME"
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        response = s3_client.get_object(Bucket=bucket, Key=key)
        lines = response['Body'].read().decode('utf-8-sig').split('\n')
        
        csv_reader = csv.reader(lines)
        headers = next(csv_reader)  # Read the first line as headers
        
        for line in csv_reader:
            if line:  # Skip empty lines
                item = {headers[i]: line[i] for i in range(len(headers))}
                print(item) # If you want to see all the items in CloudWatch Logs
                table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': 'Successfully processed {} records.'.format(len(lines) - 1)
    }
