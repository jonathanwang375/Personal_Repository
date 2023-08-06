#!/bin/bash

script_path=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
top_folder=$script_path/..
black $top_folder