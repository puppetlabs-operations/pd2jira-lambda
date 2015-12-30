# pd2jira-lambda
An AWS lambda function to handle webhooks received from PagerDuty through the AWS API gateway service

# Building
Create a virtualenv in the project directory and run the build script. It will produce as zip file that you will then upload to AWS.
```
virtualenv .
mkdir build
./build.sh
```

# Upload to AWS
This step assumes you have the aws cli configured and you have the correct access policy in place to use the AWS lambda service.
Run the following command to upload the lambda function to AWS.
```
aws lambda update-function-code --zip-file fileb://$PWD/pd2jira-lambda.zip --function-name PagerDuty2Jira
```

