#!/bin/sh
make docs lint
python3 ./scripts/check.py
