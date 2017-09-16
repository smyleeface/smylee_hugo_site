import json
#import boto3

from datetime import datetime
import logging

#from botocore.client import Config


RFC_1123_DT_STR = "%a, %d %b %Y %H:%M:%S GMT"
#   RFC 2616 = Wdy, DD Mon YYYY HH:MM:SS GMT

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    t = datetime.now().strftime(RFC_1123_DT_STR)
    #return t.strftime("%d-%b-%Y-%H")
    #{"responseText":t}
    #data ={}
    #data['responseText'] = t
    #return json.dumps(data)
    return t