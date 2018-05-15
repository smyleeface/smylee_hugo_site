import logging
import json
import boto3

from github_signature_check import GitHubSignatureCheck

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

session = boto3.Session()
ssm_client = session.client('ssm')

response = ssm_client.get_parameter(
    Name='/github/webhook/secret',
    WithDecryption=True
)
secret = response['Parameter']['Value']  # TODO: `get_parameter` permission

allowed_user_agents = ['GitHub-Hookshot', 'PostmanRuntime']


def lambda_handler(event, context):

    logging.debug(event)
    logging.debug(json.dumps(event))

    policy = {
        'principalId': 'user',
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': 'Deny',
                    'Resource': ''
                }
            ]
        }
    }

    # set the resource arn in the policy
    method_arn = event["methodArn"]
    policy['policyDocument']['Statement'][0]['Resource'] = method_arn

    user_agent = event['headers']['User-Agent'].split('/')
    logging.info(f'*** INFO: User-Agent: {user_agent}')

    if user_agent[0] in allowed_user_agents:
        policy['policyDocument']['Statement'][0]['Effect'] = 'Allow'

    # TODO (20180515, smyleeface): When API Gateway Authorizer supports sending the Body, then I can use the below
    #  code to verify. Remove compare_signatures from other lambda functions # remove the word `sha=` from the GitHub
    #
    # signature github_signature = event['headers']['X-Hub-Signature'] if '=' in github_signature: sha_name,
    # github_signature = github_signature.split('=')
    #
    # event_body = json.loads(event['body'])
    #
    # # check github signature and the generated signature
    # github_sig_check = GitHubSignatureCheck(secret, event_body, github_signature, logger)
    # if github_sig_check.compare_signatures() and event_body['commits'][0]['author']['name'] == 'smyleeface':
    #     policy['policyDocument']['Statement'][0]['Effect'] = 'Allow'

    logging.info(f'*** INFO: Generated policy: {policy}')
    return policy


