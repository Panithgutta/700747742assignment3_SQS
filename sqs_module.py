import boto3
import logging
import json
sqs=boto3.resource('sqs')
queue=sqs.create_queue(
 QueueName='SQSASSIGNMENT3'
 
 )
print("Created queue '%s' with URL=%s",'myPytonQueue',queue.url)


def send_message_to_sqs_queue(message):
    queue_name = os.environ.get('SQS_QUEUE_NAME', 'SQSASSIGNMENT3')
    response = queue.send_message(MessageBody=json.dumps(message))
    print(f"Message sent to SQS queue {queue_name}: {response.get('MessageId')}")
   message = {'key': 'value'}
send_message_to_sqs_queue('Name : Panith kumar')