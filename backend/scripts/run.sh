#!/bin/bash

env/scripts/activate
uvicorn src.main:app --reload