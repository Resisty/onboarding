#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
git fetch origin $1
git checkout $1
if [ -z "${VIRTUAL_ENV}" ]
then
	virtualenv . -p python3
	source bin/activate
fi
