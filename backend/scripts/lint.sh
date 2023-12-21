#!/bin/bash

set -e
set -x

mypy app
ruff app --fix
black app
isort app