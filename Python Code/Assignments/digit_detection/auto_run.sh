#!/bin/bash

# Define the arrays
array1=(500 500 60 80)
array2=(0.0001 0.0001 0.00005 0.00005)
array3=(4 6 3 4)

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
    python3 digit_detection_pytorch.py $arg1 $arg2 $arg3 && curl -d "Model $i is done" ntfy.sh/byreddy_ml
done
sleep 1
curl -d "All models done" ntfy.sh/byreddy