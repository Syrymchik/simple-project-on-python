import boto3
import botocore

if __name__ == '__main__':

    f = open('value3.txt', 'w')

    for i in range(10):
        f.write("Line %d \n" % (i + 1))

    f.close()

    BUCKET_NAME = 'telecomecloudcomputing'
    filename = 'value3.txt'
    filename2 = 'value5.txt'

    s3 = boto3.client('s3')

    s3.upload_file(filename, BUCKET_NAME, filename2)

    s32 = boto3.resource('s3')
    try:
        s32.Bucket(BUCKET_NAME).download_file(filename2, 'value5.txt')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise


    r = open('value5.txt', 'r')

    if r.mode == 'r':
        content = r.read()
        print(content)
        r.close()