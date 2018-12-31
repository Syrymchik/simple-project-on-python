import boto3

from Sqs import GetMessage

url = 'https://sqs.us-east-1.amazonaws.com/706296125273/mybucket207'

if __name__ == '__main__':

    s3 = boto3.resource('s3')


    filename = 'file.txt'
    bucket_name = 'telecomecloudcomputing'

    s3.upload_file(filename, bucket_name, filename)

    sqs_client = boto3.client('sqs')
    for message in GetMessage.GetMessage.get_messages_from_queue('https://sqs.us-east-1.amazonaws.com/706296125273/mybucket207'):
        print('************************************************************')
    print(message['Body'])