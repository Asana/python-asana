#!/usr/bin/env python3

"""
This script runs a Flask server that handles webhook requests from Asana,
and sends a Slack notification whenever the server receives and event indicating
that a milestone was completed.

Instructions:
1. Set the ASANA_ACCESS_TOKEN environment variable to your Personal Access Token
2. Set the SLACK_TOKEN environment variable to your Slack API token
3. Create a webhook using for your project using manage_webhooks.py
"""

import hmac
import os
import sys
from hashlib import sha256

import asana
from flask import Flask, Response, abort, request
import slack

SECRET_FILE = "/tmp/asana_webhook_secret"

# We need an Asana client to fetch the full names of tasks and users
# since webhook events are "skinny"
client = asana.Client.access_token(os.environ.get("ASANA_ACCESS_TOKEN"))
slack_client = slack.WebClient(token=os.environ.get("SLACK_TOKEN"))

app = Flask(__name__)


def load_webhook_secret():
    with open(SECRET_FILE, "rb+") as f:
        return f.read().strip()


def set_webhook_secret(value):
    with open(SECRET_FILE, "w+") as f:
        f.write(value)


def validate_request(req):
    # Takes a flask request and computes a SHA256 HMAC using the webhook
    # secret we received from Asana and compares it with the signature provided
    # in the request as described in https://developers.asana.com/docs/#asana-webhooks.
    # Returns whether the two signatures match.

    request_signature = request.headers.get("X-Hook-Signature")
    computed_signature = hmac.new(
        load_webhook_secret(), msg=req.data, digestmod=sha256
    ).hexdigest()

    return hmac.compare_digest(computed_signature, request_signature)


def notify_slack(user, milestone):
    # Send a message to Slack for a milestone completion
    message = "{} just completed the milestone {}!".format(
        user.get("name"), milestone.get("name")
    )
    print('Sending message to Slack: "{}"'.format(message))
    try:
        slack_client.chat_postMessage(channel="#asana-notifications", text=message)
    except slack.errors.SlackApiError:
        print("Error sending message to Slack.")


@app.route("/receive_asana_webhook", methods=["POST"])
def receive_asana_webhook():

    request_secret = request.headers.get("X-Hook-Secret")
    if request_secret:
        # On webhook creation, the server will be sent a request for which we respond with 200 OK
        # and a matching X-Hook-Secret header to confirm that we are accepting webhook requests

        # Note: resetting the local webhook secret whenever we get a new request to change
        set_webhook_secret(request_secret)

        resp = Response()
        resp.headers["X-Hook-Secret"] = load_webhook_secret()
        return resp
    elif not validate_request(request):
        # Return 403 Forbidden if the request signature doesn't match
        abort(403)

    events = request.json.get("events")
    for event in events:
        # Check if the event is the completion of a milestone
        if (
            event["resource"].get("resource_subtype") == "marked_complete"
            and event["parent"].get("resource_subtype") == "milestone"
        ):
            # The event only provides an id, so we need to get the full task
            # and user objects to use in the notification
            gid = event["parent"].get("gid")
            user_id = event["user"].get("gid")
            user = client.users.find_by_id(user_id)
            milestone = client.tasks.find_by_id(gid)
            notify_slack(user, milestone)

    return Response()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
