#!/bin/bash

pipreqs . --force
PACKAGE_DIRECTORY="dist"
python setup.py sdist bdist_wheel
twine check $PACKAGE_DIRECTORY/*
twine upload $PACKAGE_DIRECTORY/* 
rm -rf build
rm -rf dist
rm -rf *.egg-info

