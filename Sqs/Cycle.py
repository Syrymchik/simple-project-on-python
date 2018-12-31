import statistics
import time
import json
import boto3
import math

sqs = boto3.resource('sqs')
s3 = boto3.client('s3')
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
    queue = sqs.get_queue_by_name(QueueName='requestQueue')
    queue2 = sqs.get_queue_by_name(QueueName='responseQueue')

    for message in queue.receive_messages(MessageAttributeNames=['Author']):



        data = json.loads(message.body)
        print(data['integers'])
        result = {
            "name": data['name'],
            "min": int(min(data['integers'])),
            "max": int(max(data['integers'])),
            "mean":  float(statistics.mean(data['integers'])),
            "median": float(statistics.median(data['integers'])),
        }

        print(result)

        message.delete()

        response = queue2.send_message(MessageBody='%s' %result)
        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))
        print(min(data['integers'])) # 0
        print(max(data['integers'])) # 50
        print(statistics.mean(data['integers'])) # 25.0
        print(statistics.median(data['integers'])) # 25

        f = open(filename, 'a')
        f.write('Result of handle - %s\n' %result)
        f.close()

        val += 1
        print('Val = %d' %val)

        if val == 10:
            s3.upload_file(filename, BUCKET_NAME, filename)
            val %= 10
            print('uploded file - %s\n' %filename)

    print('end sqs operation')
    time.sleep(7)

