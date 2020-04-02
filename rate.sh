#!/bin/bash

echo -n $1 " "

egrep "Input rate | Output rate" $1  | sed 's/(//g' | sed 's/bps//g' | sed 's/pps)//g' | awk '$1 ~/Input/ { input += $4 } $1 ~/Output/ { output += $4 } END {printf "Input: %f - Output %f\n", input/(NR/2)/1000000000, output/(NR/2)/1000000000 }'
