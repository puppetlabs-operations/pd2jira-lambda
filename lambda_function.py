from __future__ import print_function
from jira import JIRA

import json

print('Loading function')


summary_service_template = """
Service {servicedesc} on host {host} is {state}
"""
summary_host_template = """
Host/zone {host} is {state}
"""
description_template = """
Incident URL:
{incident_url}
"""


def lambda_handler(event, context):
    with open('./config.json') as f:
        config = json.loads(f.read())
    print("Received event: " + json.dumps(event, indent=2))
    jira = JIRA(config['jira_url'], basic_auth=(config['jira_user'], config['jira_password']))
    print(jira)
    for message in event['messages']:
        if message['type'] == 'incident.trigger' and message['data']['incident']['status'] == 'triggered':
            if message['data']['incident']['trigger_summary_data']['pd_nagios_object'] == 'service':
                issue_summary = summary_service_template.format(servicedesc=message['data']['incident']['trigger_summary_data']['SERVICEDESC'],
                                                                host=message['data']['incident']['trigger_summary_data']['HOSTNAME'],
                                                                state=message['data']['incident']['trigger_summary_data']['SERVICESTATE'])
                issue_description = description_template.format(incident_url=message['data']['incident']['html_url'])
            try:
                incident_ticket = jira.create_issue(project=config['jira_project'],
                                                    summary=issue_summary,
                                                    description=issue_description,
                                                    issuetype={'name': config['jira_ticket_type']})
            except jira.JIRAError as e:
                print(e.text)
