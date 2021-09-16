#!/bin/bash

set -euxo pipefail

mount

mkdir /sys/fs/cgroup/memory

mount -t cgroup memory -o memory /sys/fs/cgroup/memory
