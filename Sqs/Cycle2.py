import statistics
import time
import json
import boto3
import botocore
from PIL import Image, ImageFilter

sqs = boto3.resource('sqs')
s3 = boto3.client('s3')
s3R = boto3.resource('s3')
filename = 'cloudData.txt'
BUCKET_NAME = 'telecomecloudcomputing'
val = 0

print('*******************************************************************************************')
print('*******************************************************************************************')
print('*****       ****   ********         ***  *****  ***       ********     *****     **********')
print('***    ***   ***   ********  *****  ***  *****  ***  ****   *****       ***       *********')
print('***  ***********   ********  *****  ***  *****  ***  *****  ******       *       **********')
print('***  ***********   ********  *****  ***  *****  ***  *****  *******             ***********')
print('***   ******  **   ********  *****  ***  *****  ***  ****   ********          *************')
print('*****       ****        ***         ****       ****       *************     ***************')
print('*******************************************************************************************')
print('*******************************************************************************************')

while True:

    print('*******************************************************************************************')
    print('*******************************************************************************************')
    print('*******************************************************************************************')
    print('every 7 second')
    print('start sqs operation')
    queue = sqs.get_queue_by_name(QueueName='inbox')
    queue2 = sqs.get_queue_by_name(QueueName='outbox')

    for message in queue.receive_messages(MessageAttributeNames=['Author']):

        data1 = message.body
        print(data1)

        result = 'processed-%s' %data1
        print(result)

        message.delete()

        try:
            s3R.Bucket(BUCKET_NAME).download_file(data1, result)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                raise

        image = Image.open(result)
        image = image.filter(ImageFilter.CONTOUR)
        image.save(result, 'JPEG')
        # image.show()

        s3.upload_file(result, BUCKET_NAME, result)
        print('uploded file - %s\n' %result)

        response = queue2.send_message(MessageBody='%s' %result)
        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))


    print('end sqs operation')
    time.sleep(7)

