

######### test case of creating sso user ##############
# During the creation you can able to create single user at a time and add that user to multple groups
{
  "RequestType": "Update", # Create , Update and Delete
  "ResponseURL": "https://httpbin.org/put", 
  "StackId": "arn:aws:cloudformation:region:account:stack/test-stack/abcd",
  "RequestId": "unique-create-request-id",
  "LogicalResourceId": "MySSOUser",
  "PhysicalResourceId": "reandomly-generated",
  "ResourceProperties": {
    "IdentityStoreId": "xxxxxxxxxx",
    "UserName": "xxxxxxxxx",
    "UserEmail": "xxxxxxxxxxx",
    "FirstName": "qwerty",
    "LastName": "kumar",
    "DisplayName": "qwerty",
    "GroupName": ["xxxx","xxxx"] #
  }
}


############ test case for assgin existing users to multiple groups ###########
{
  "RequestType": "Update",
  "ServiceToken": "arn:aws:lambda:us-east-1:123456789012:function:assign-user-group-lambda",
  "ResponseURL": "https://cloudformation-custom-resource-response.example.com",
  "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/example-stack/abcd1234",
  "RequestId": "unique-create-request-id",
  "LogicalResourceId": "ManageSSOUserGroupMembership",
  "ResourceProperties": {
    "ServiceToken": "assgin-user-lambda-arn",
    "IdentityStoreId": "xxxxxxxxx",
    "GroupName": "xxxxxxxxxx",
    "Usernames": ["demo123","xxxxx"],
    "Operation": "add" # remove
  }
}


--------------- creating ssogroup-----------------
{
  "RequestType": "Delete",
  "ResponseURL": "https://httpbin.org/put", 
  "StackId": "arn:aws:cloudformation:region:account:stack/test-stack/abcd",
  "RequestId": "unique-create-request-id",
  "LogicalResourceId": "MySSOUser",
  "PhysicalResourceId": "d8f133a0-f041-70b8-92aa-e0509001299d",
  "ResourceProperties": {
    "IdentityStoreId": "xxxxxxxxxxxx",
    "PermissionSetArn": "xxxxxxxxxxxxxxxxxx",
    "InstanceArn": "xxxxxxxxxxxxxxxxxxxxxxx",
    "ApplicationArns": ["xxxxxxxxx","xxxxxxxxxxxx"],
    "AccountIds": ["xxxxxxxx","xxxxxxxxxxx"],
    "GroupName": "xxxxxxx"
  }
}

