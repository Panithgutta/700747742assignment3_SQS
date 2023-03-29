import json

with open('config.json', 'r') as f:
    config = json.load(f)

sqs_queue_name = config['SQSASSIGNMENT3']
