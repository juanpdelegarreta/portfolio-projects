#!/bin/bash

# Define loop count for controlled execution time
iterations=1000000000000

# Efficiently check for prime numbers within iterations
for ((i=2; i*i<=iterations; i++)); do
  # Optimized prime check using divisibility rule
  for ((j=2; j*j<=i; j++)); do
    if [[ $((i % j)) -eq 0 ]]; then
      break
    fi
  done
  # Optional to utilize prime numbers (e.g., store in array)
  # if [[ $is_prime ]]; then
  #   prime_numbers+=("$i")
  # fi
done

echo "Done! Script completed $iterations iterations."
