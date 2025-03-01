#!/usr/bin/env python3
"""
An example script showing ways to manage your webhooks using the
python-asana client library, see README.md or run ./manage_webhooks.py -h
for usage examples
"""

import argparse
import os

import asana

WORKSPACE_ID = "15793206719"

client = asana.Client.access_token(os.environ.get("ASANA_ACCESS_TOKEN"))
WORKSPACE_NAME = client.workspaces.find_by_id(WORKSPACE_ID).get("name")


def list_webhooks():
    print(
        "Displaying webhooks you own associated with workspace: {}".format(
            WORKSPACE_NAME
        )
    )
    webhooks = client.webhooks.get_all({"workspace": WORKSPACE_ID})
    for w in webhooks:
        print(w)


def delete_webhook(gid):
    print("Deleting webhook: {}".format(gid))
    client.webhooks.delete_by_id(gid)


def delete_all_webhooks():
    print(
        "Deleting all webhooks you own associated with workspace: {}".format(
            WORKSPACE_NAME
        )
    )
    webhooks = client.webhooks.get_all({"workspace": WORKSPACE_ID})
    for w in webhooks:
        client.webhooks.delete_by_id(w.get("gid"))


def create_webhook(resource, target):
    print(
        "Creating webhook on {}, make sure that the server at {} is ready to accept requests!".format(
            resource, target
        )
    )
    client.webhooks.create({"resource": resource, "target": target})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        help="What you want to do with Asana webhooks", dest="command", required=True
    )

    list_parser = subparsers.add_parser("list", help="List existing webhooks")

    create_parser = subparsers.add_parser("create", help="Create a new webhook")
    create_parser.add_argument(
        "--resource",
        type=str,
        help="A resource ID to subscribe to. The resource can be a task or project",
        required=True,
    )
    create_parser.add_argument(
        "--target",
        type=str,
        help="The webhook URL to receive the HTTP POST",
        required=True,
    )

    delete_parser = subparsers.add_parser(
        "delete", help="Delete one or all existing webhooks"
    )
    delete_group = delete_parser.add_mutually_exclusive_group(required=True)
    delete_group.add_argument(
        "--id", type=str, help="The ID of the webhook you want to delete"
    )
    delete_group.add_argument("--all", action="store_true")

    args = parser.parse_args()

    if args.command == "list":
        list_webhooks()
    elif args.command == "create":
        create_webhook(args.resource, args.target)
    elif args.command == "delete":
        if args.all:
            delete_all_webhooks()
        else:
            delete_webhook(args.id)
