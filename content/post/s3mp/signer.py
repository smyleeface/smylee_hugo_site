#import boto3
from base64 import b64encode
import hmac, sha

import logging

#from botocore.client import Config

# Get the service client with sigv4 configured
#s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
#ENCRYPTED_EXPECTED_TOKEN = "<kmsEncryptedToken>" # Enter the base-64 encoded, AWS secret key token (CiphertextBlob)

##  kms = boto3.client('kms',region_name='us-east-1', config=Config(signature_version='s3v4'))
#expected_token = kms.decrypt(CiphertextBlob = b64decode(ENCRYPTED_EXPECTED_TOKEN))['Plaintext']

keyId = "arn:aws:iam::952671759649:user/pramertsf"
customer_key=" 9526-7175-9649"
secret ="ADkfV3JIYWUDwaeBoFbv151PxAdeb91I9u53i+JD"  ##this MUST match client side access ID given
#meta = kms.describeKey(keyId=keyId)['KeyMetadata'];

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(event)
    if not event['to_sign']:
        raise Exception('Unauthorized')
    to_sign = str(event['to_sign'])
    # raw encoding... >>>>>>>>>
 ## signature = b64encode(hmac.new(ENCRYPTED_EXPECTED_TOKEN, to_sign, sha).digest())
    #self.response.headers['Content-Type'] = "text/HTML"
    #self.response.out.write(signature)
    # Generate the URL to get 'key-name' from 'bucket-name'
    #S3>>>>>>>>>
    #url = s3.generate_presigned_url(ClientMethod='get_object',Params={'Bucket': 'bucket-name','Key': 'key-name' })
    ####
    ###  kms.generate_presigned_url(ClientMethod, Params=None, ExpiresIn=3600, HttpMethod=None)


   ## data_key_req = kms.generate_data_key( KeyId=keyId, KeySpec='AES_256' )
   ## data_key = data_key_req['Plaintext']
   ## data_key_ciphered = data_key_req['CiphertextBlob']

    #signature = b64encode(hmac.new(data_key, to_sign, sha).digest())


    signature = b64encode(hmac.new(secret, to_sign, sha).digest())

    #encrypt_file(filepath, data_key)

  ## signature=b64encode(data_key_ciphered)

    #signature = base64.b64encode(hmac.new(data_key, to_sign, sha).digest())
   
    #s3 = boto3.client('s3')
    #s3.put_object(Bucket='mybucketname', Body=open('test.txt.enc', 'r'), Key='test.txt', Metadata={'encryption-key': base64.b64encode(data_key_ciphered)})
   
   #{"signiture":signiture}
   #{"Payload":signiture}
    return signature