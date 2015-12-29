#!/bin/bash
cp -R lib/python2.7/site-packages/* ./build
cp lambda_function.py ./build
cd build
zip -r ../pd2jira-lambda.zip ./*
cd ..
aws lambda update-function-code --zip-file fileb://$PWD/pd2jira-lambda.zip --function-name PagerDuty2Jira
