#!/bin/bash

python ./test.py &
PID2=$!
echo "Running process: $PID2"

sleep 2

python ./sens.py &
PID1=$!
echo "Running process: $PID1"

wait $PID1
echo "Process $PID1 finished."

wait $PID2
echo "Process $PID2 finished."

echo "Ending container sensors."
