#!/bin/bash

PROBLEM=${1%/}

echo "Running tests for $PROBLEM (left is output, right is expected)"
echo

for file in $PROBLEM/tests/*.in; do
    echo "-- Test case $file:"
    cat $file | python $PROBLEM/main.py | diff - ${file/.in/.out} -y
    echo
done
