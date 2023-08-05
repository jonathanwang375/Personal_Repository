#!/bin/bash

script_path=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
echo "$script_path" >&2
top_folder=$script_path/..
for d in ../*; do
    echo $d
done
