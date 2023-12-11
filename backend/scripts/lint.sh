#!/bin/bash

set -e
set -x

mypy src tests
ruff src tests --fix
black src tests
isort src tests