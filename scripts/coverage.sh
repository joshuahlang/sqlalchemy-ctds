#!/bin/sh -e

pip install --no-cache-dir -v -e .

mkdir coverage

# Outputs data to ".coverage"
coverage run --branch --source 'sqlalchemy-ctds' run_tests.py
coverage report -m --skip-covered

coverage xml
cp coverage.xml coverage

