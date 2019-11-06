# Overview

This project shows how Asana webhooks can be used to send a notification to Slack whenever a milestone is completed.
It also contains examples of how to manage webhooks through the Python Asana client.

## Webhooks server
Start the server before creating any webhooks
```
ASANA_ACCESS_TOKEN=<your Asana PAT> SLACK_TOKEN=<your Slack API token> ./server.py 
```

## Manage Webhooks
List existing webhooks:
```
ASANA_ACCESS_TOKEN=<your Asana PAT> ./manage_webhooks.py list 
```

Create a new webhook:
```
ASANA_ACCESS_TOKEN=<your Asana PAT> ./manage_webhooks.py create --resource <resource id> --target <target url>
```

Delete a webhook by ID:
```
ASANA_ACCESS_TOKEN=<your Asana PAT> ./manage_webhooks.py delete --id <webhook id>
```

Delete ALL your webhooks:
```
ASANA_ACCESS_TOKEN=<your Asana PAT> ./manage_webhooks.py delete --all
```
