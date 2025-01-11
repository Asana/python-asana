# Overview

This project shows how Asana webhooks can be used to send a celebratory message to Slack whenever a milestone is completed.
It also contains examples of how to manage webhooks through the Python Asana client.

## Webhooks server
Start the server before creating any webhooks. **The server needs to be DNS-addressable or have a public IP address for Asana to reach it. For development, you can use [ngrok](https://ngrok.com/) to quickly expose to your localhost to the web.**

```
ASANA_ACCESS_TOKEN=<your Asana PAT> SLACK_TOKEN=<your Slack API token> ./server.py 
```

## Manage Webhooks
**List existing webhooks:**
```
ASANA_ACCESS_TOKEN=<your Asana PAT> ./manage_webhooks.py list 
```

**Create a new webhook:**
```
ASANA_ACCESS_TOKEN=<your Asana PAT> ./manage_webhooks.py create --resource <resource id> --target http://<public server address>:3000/receive_asana_webhook
```

**Note:** In this example, the target URL would point to the Flask endpoint defined in `server.py`.



**Delete a webhook by ID:**
```
ASANA_ACCESS_TOKEN=<your Asana PAT> ./manage_webhooks.py delete --id <webhook id>
```

**Delete ALL your webhooks:**
```
ASANA_ACCESS_TOKEN=<your Asana PAT> ./manage_webhooks.py delete --all
```
