#!/usr/bin/env bash

##############################################################################
# diff-example.sh
#
#   Custom diff command which strips the first N lines from each file
# before comparing the files
#
# Usage:
#   bash diff-example.sh n input-file-1 input-file-2
##############################################################################

n1=$1
n2=$n1
input1=$2
input2=$3

diff -q <(tail -n +"${n1}" "${input1}") <(tail -n +"${n2}" "${input2}")
