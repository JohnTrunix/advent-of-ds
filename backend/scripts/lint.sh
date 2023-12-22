#!/bin/bash

set -e
set -x

mypy app tests
ruff app tests --fix
black app tests
isort app tests