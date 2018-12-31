import boto3


class GetMessage:

    @staticmethod
    def get_messages_from_queue(queue_url):
        sqs_client = boto3.client('sqs')

        messages = []

        while True:
            resp = sqs_client.receive_message(
                QueueUrl=queue_url,
                AttributeNames=['All'],
                MaxNumberOfMessages=10
            )

            try:
                messages.extend(resp['Messages'])
            except KeyError:
                break

            entries = [
                {'Id': msg['MessageId'], 'ReceiptHandle': msg['ReceiptHandle']}
                for msg in resp['Messages']
            ]

            resp = sqs_client.delete_message_batch(
                QueueUrl=queue_url, Entries=entries
            )

            if len(resp['Successful']) != len(entries):
                raise RuntimeError(
                    f"Failed to delete messages: entries={entries!r} resp={resp!r}"
                )

        return messages

# if __name__ == '__main__':
#
#     sqs_client = boto3.client('sqs')
#
#
#     for message in get_messages_from_queue('https://sqs.us-east-1.amazonaws.com/706296125273/mybucket207'):
#         print('************************************************************')
#         print(message['Body'])
