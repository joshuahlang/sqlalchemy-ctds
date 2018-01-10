#!/bin/sh -e

pip install --no-cache-dir -v -e .

python setup.py -v test
