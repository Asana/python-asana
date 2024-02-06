# Test Build


This directory contains tests that are meant to be ran locally

1. Install install dependencies `pip install -r requirements.txt`
2. Create a `.env` file in the root directory and set environment variables
```
PERSONAL_ACCESS_TOKEN=<YOUR_ASANA_PERSONAL_ACCESS_TOKEN>
TEAM_GID=<YOUR_TEAM_GID>
TEXT_CUSTOM_FIELD_GID=<YOUR_TEXT_CUSTOM_FIELD_GID> -> NOTE: make sure that there is at least one task that has this custom field and the value of the custom field on that task is `custom_value`
USER_GID=<YOUR_USER_GID>
WORKSPACE_GID=<YOUR_WORKSPACE_GID>
```
3. Run tests `python -m unittest discover ./build_tests`
