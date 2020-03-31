 #!/bin/bash
 
 rm $1-graph.txt 
 ./show_cpu.sh $1 | grep '^[0-9+]' | tail -n 39 | awk '{ print $2, $3 }' > $1-graph.txt 
 rm $1-graph.txt-chart.xlsx
 python3 ./chart_cpu.py $1-graph.txt