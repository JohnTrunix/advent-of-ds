#!/bin/bash

set -e
set -x

pytest -vv --cov=src --cov-report=term-missing --cov-fail-under=80 tests/