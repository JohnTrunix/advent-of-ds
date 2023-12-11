#!/bin/bash

source env/scripts/activate
uvicorn src.main:app --reload