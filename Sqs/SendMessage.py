# Get the service resource
import boto3

sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='mybucket207')

# Create a new message
response = queue.send_message(MessageBody='2020worl12d')

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))