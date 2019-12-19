REGION = 'us-east-1';
IDENTITY_POOL_ID = 'us-east-1:e2b14a41-c427-4bb5-b192-61bc80c999b2'; //us-east-1:ab59d458-d732-482f-b652-b20ac9e04fec
USER_POOL_ID = 'us-east-1_WZSS9Ogmv'; //us-east-1_yUcZNKVNA
CLIENT_ID = '22ekj403vr6nd21n1o12cp5sa2'; //145fodr59njru69811g2n6r3sh

//cognito setup
AWS.config.region = REGION; // Region
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: IDENTITY_POOL_ID // your identity pool id here
});

AWSCognito.config.region = REGION;
AWSCognito.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: IDENTITY_POOL_ID,
});

// Need to provide placeholder keys unless unauthorised user access is enabled for user pool
// AWSCognito.config.update({accessKeyId: 'anything', secretAccessKey: 'anything'})

var poolData = {
    UserPoolId : USER_POOL_ID,
    ClientId : CLIENT_ID
};
var userPool = new AWSCognito.CognitoIdentityServiceProvider.CognitoUserPool(poolData);