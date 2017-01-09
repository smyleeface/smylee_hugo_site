import boto3


def clean_s3():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('smylee.com.updates')
    response = bucket.objects.delete()
    for deleted in response['Deleted']:
        print deleted['Key']
    for errors in response['Errors']:
        print errors['Key']
        print errors['Code']
        print errors['Message']


if __name__ == '__main__':
    clean_s3()
