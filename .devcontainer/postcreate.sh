#!/bin/zsh

# Install dependencies
poetry install

# Install precommit hooks
pre-commit install && pre-commit install -t commit-msg
