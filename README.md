## Calculate talus drops
	./talus.sh .//VRSECGWL01/2020-03-28-dina.txt 

##Show ESP and Clear Text Fragments
 	./show_tunnels.sh .//VRSECGWL01/2020-03-28-dina.txt | grep "Tunnels with ESP/AH frag Rx"
 	./show_tunnels.sh .//VRSECGWL01/2020-03-28-dina.txt | grep "Tunnels with IPv4 frag Tx"

##Show Input / Output counters (packets & bytes)
	python3 new_intfcnt.py .//VRSECGWL01/2020-03-28-dina.txt 

##Show input/output rates
	egrep "Input rate | Output rate" ././/VRSECGWL01/2020-03-28-dina.txt  | sed 's/(//g' | sed 's/bps//g' | sed 's/pps)//g'
