#!/bin/bash
zip -r pd2jira-lambda.zip lambda_function.py 
aws lambda update-function-code --zip-file fileb://$PWD/pd2jira-lambda.zip --function-name PagerDuty2Jira
