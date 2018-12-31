import time
import json
import boto3
import math

sqs = boto3.resource('sqs')

while True:
    print('every 5 second \n start sqs operation')
    queue = sqs.get_queue_by_name(QueueName='requestQueue')
    queue2 = sqs.get_queue_by_name(QueueName='responseQueue')

    for message in queue.receive_messages(MessageAttributeNames=['Author']):

        data = json.loads(message.body)
        print(data['integers'])
        sumValue = sum(data['integers']);
        avgValue = sumValue / 2
        print('sum = {0}, avg = {1}'.format(sumValue, avgValue))

        result = {
            "name": data['name'],
            "avg": int(avgValue),
            "sum": int(sumValue),
        }
        # result = json.dump(result)
        print(result)

        # print('{0}{1}{2}'.format(data.num1, data.name, data.num2))

        # Let the queue know that the message is processed
        message.delete()

        response = queue2.send_message(MessageBody='%s' %result)
        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))


    print('end sqs operation')




    time.sleep(5)

