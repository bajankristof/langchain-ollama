#!/usr/bin/env bash

ollama serve &
pid=$!

for i in {1..10}; do
    ollama ls > /dev/null
    if [ $? -eq 0 ]; then
        break
    fi
    sleep 1
done

set -e

ollama run $MODEL

wait -n

exit $?
