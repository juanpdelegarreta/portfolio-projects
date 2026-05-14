#!/bin/bash

# IP to ping
IP="8.8.8.8"  

# Number of pings
COUNT=3

# Log file  
LOGFILE="/var/log/pinger.log"

# Perform pings
ping -c $COUNT $IP > ping_output.txt

# Grep average RTT 
average=$(grep "rtt" ping_output.txt | awk '{print $4}' | cut -d '/' -f 2)

# Remove units  
ms=$(echo $average | cut -d '.' -f 1) 

# Timestamp
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Write ping time and timestamp to log 
echo "$ms $TIMESTAMP" >> $LOGFILE  

# Clean up
rm ping_output.txt
