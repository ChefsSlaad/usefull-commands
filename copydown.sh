#!/usr/bin/env bash

for f in *; do
    if [[ -d "$f" && ! -L "$f" ]]; then
        rsync -a  "$f"/* . && rm -r "$f"/
    fi
done
