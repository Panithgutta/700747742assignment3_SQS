import boto3
import logging
import json
sqs=boto3.resource('sqs')
queue=sqs.create_queue(
 QueueName='SQSASSIGNMENT3'
 
 )
print("Created queue '%s' with URL=%s",'myPytonQueue',queue.url)


def send_message_to_sqs(message):
    response = queue.send_message(MessageBody=message)
    print(f"Message sent with ID: {response['MessageId']}")



send_message_to_sqs("Hello world")