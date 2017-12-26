#!/bin/sh

# From: https://stackoverflow.com/a/19258421/19818

zip $@
rc=$?

if [[ rc -eq 12 ]]; then
    exit 0
fi
exit $rc
