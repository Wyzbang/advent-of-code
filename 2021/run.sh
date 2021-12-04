#!/bin/bash

for VARIABLE in 1 2 3
do
	cd day$VARIABLE
	python3 day$VARIABLE.py
	cd ..
  echo
done
