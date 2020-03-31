#!/bin/bash

echo -n $1 " "
awk '/show security flow session tunnel summary/,/^node1/ { print $0 }' $1 


