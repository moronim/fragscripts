#!/bin/bash

echo -n $1 " "
awk '/show talus 1 drop/,/show interfaces reth0 statistics/ { print $0 }' $1 | sed 's/_//g' | awk '/^show talus 1/ { buf = "" } { buf = buf "\n" $0 } END { print buf }' | awk 'BEGIN {total = 0} {for (i=5;i<NF;i++) { total += $i}} END {printf ("%d \n", total)}'


