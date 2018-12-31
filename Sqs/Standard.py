from sqs_listener import SqsListener


def run_my_function(param, param1):
    pass


class MyListener(SqsListener):
    def handle_message(self, body, attributes, messages_attributes):
        run_my_function(body['param1'], body['param2'])

listener = MyListener('https://sqs.us-east-1.amazonaws.com/706296125273/mybucket207', error_queue='https://sqs.us-east-1.amazonaws.com/706296125273/mybucket207', region_name='us-east-1')
listener.listen()