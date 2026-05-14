
#!/bin/bash

total_count=1000000000
# Adjust speed based on desired demonstration time
sleep_time=0.00

for ((i=1; i<=$total_count; i++)); do
  # Simulate progress with "#" characters
  echo  $i $(date +%H:%M:%S.%N)

  # Adjust sleep time for desired progress speed
  sleep "$sleep_time"
done

echo "\nDone! (Simulation completed)"#!/bin/bash

