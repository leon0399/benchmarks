#!/bin/bash

set -euxo pipefail

./setup-cgmemtime.sh

tail -F anything
