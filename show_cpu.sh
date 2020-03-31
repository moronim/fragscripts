#!/bin/bash

echo -n $1 " "
awk '/show i386 cpu/,/show usp flow sess sum win/ { print $0 }' $1 


