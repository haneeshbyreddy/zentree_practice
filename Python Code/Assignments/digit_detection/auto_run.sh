#!/bin/bash

# Define the arrays
array1=(100 50 200 400 500)
array2=(0.001 0.001 0.001 0.001 0.001)
array3=(10 10 15 20 5)

# Determine the length of the arrays (assuming all arrays have the same length)
length=${#array1[@]}

# Loop over each index
for (( i=0; i<length; i++ )); do
    # Select elements based on the index
    arg1=${array1[$i]}
    arg2=${array2[$i]}
    arg3=${array3[$i]}

    # Print the arguments (for debugging)
    echo "Running with arguments: $arg1 $arg2 $arg3"

    # Run the Python script with the selected arguments
    python3 digit_detection_pytorch.py $arg1 $arg2 $arg3
done