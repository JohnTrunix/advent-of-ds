#!/bin/bash

set -e
set -x

pytest -vv --cov=app --cov-report=term-missing --cov-fail-under=80 tests/