#!/bin/zsh

# Install dependencies
poetry install --with=dev

# Allow precommit to install properly
git config --global --add safe.directory /workspaces/sphinx-charts

# Install precommit hooks
pre-commit install && pre-commit install -t commit-msg
