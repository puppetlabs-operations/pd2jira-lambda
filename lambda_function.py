from __future__ import print_function
from jira import JIRA

import json

print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    return event
    #raise Exception('Something went wrong')
