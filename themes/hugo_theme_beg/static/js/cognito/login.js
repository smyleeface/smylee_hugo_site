 //login form
$('#loginform').submit(function(ev) {
    ev.preventDefault(); // to stop the form from submitting
    $un = $( "#un" ).val();
    $pw = $( "#pw" ).val();
    console.log($un, $pw);
    /* Validations go here */


    var authenticationData = {
        Username : $un,
        Password : $pw,
    };
    var authenticationDetails = new AWSCognito.CognitoIdentityServiceProvider.AuthenticationDetails(authenticationData);
    var userData = {
        Username : $un,
        Pool : userPool
    };
    var cognitoUser = new AWSCognito.CognitoIdentityServiceProvider.CognitoUser(userData);
     cognitoUser.authenticateUser(authenticationDetails, {
        onSuccess: function (result) {
            console.log('access token + ' + result.getAccessToken().getJwtToken());
            accessToken = result.getAccessToken().getJwtToken();
            //send result token to lambda function to verify that the token generated on this page is the same token
            $.ajax({
                url: "https://0cfjk73bvj.execute-api.us-east-1.amazonaws.com/prod/testing",
                contentType: "application/json",
                dataType: "text",
                type: "POST",
                data: { "Username": $un, "Pool": USER_POOL_ID, "Token": accessToken, "Region": REGION, "IdentityPoolId": IDENTITY_POOL_ID },
                error: function(jqXHR, textStatus, errorThrown) {
                    console.log(errorThrown);
                    console.log(textStatus);
                    console.log(jqXHR);
                    $( "#alert_message" ).html('<div class="alert alert-danger" role="alert">Token not correct, please try again.</div>');
                },
                success: function(data, textStatus, jqXHR) {
                    //if token submitted matches, otherwise error
                    console.log(data);
                    console.log(textStatus);
                    console.log(jqXHR);
                    $("#alert_message").html('<div class="alert alert-success" role="alert">Login Successful</div>');
                    $("#un, #pw, #submitbutton").attr("disabled","disabled");
                }
            })
        },

        onFailure: function(err) {
            // console.log(err);
            $( "#alert_message" ).html('<div class="alert alert-danger" role="alert">Incorrect username or password.</div>');
        },

    });


});