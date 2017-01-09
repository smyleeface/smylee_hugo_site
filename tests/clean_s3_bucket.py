import base64
import boto3


def kms_decrypt(secret_key):
    kms = boto3.client('kms')
    response = kms.decrypt(CiphertextBlob=base64.b64decode(secret_key))
    secret = response['Plaintext']
    return secret


def clean_s3():
    access_key = 'AKIAJ7S3FKFV55L3GKSQ'
    secret_key = 'AQECAHhC2ka8BPeHckHRaHVXFFQT7C1GRB8vlWpPeDcwW1pOfAAAAIcwgYQGCSqGSIb3DQEHBqB3MHUCAQAwcAYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzVqpvbTZPVTSVvO9ICARCAQ2m9ib/UFAB/iPXkq+LBUr4Z0hJHj0auNaK1o45f8PSVsAhRWuYzf6qLNBp8n0s5jikpKy/N8hTemaaILWaBNxNMH2Y='
    s3 = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=kms_decrypt(secret_key))
    bucket = s3.Bucket('smylee.com.updates')
    response = bucket.objects.delete()
    for deleted in response:
        print deleted['Key']
    for errors in response:
        print errors['Key']
        print errors['Code']
        print errors['Message']


if __name__ == '__main__':
    clean_s3()
