#!/bin/bash

# Load the dataset
# python -m synergy get $DATASET

# prints
echo "Running simulation..."
echo "DATASET: $DATASET"
echo "SETTINGS: $SETTINGS"
echo "SIMULATION: $SIMULATION"
echo "SIMULATION_ID: $SIMULATION_ID"

# Run the simulation
asreview simulate $DATASET -s $SIMULATION $SETTINGS

# Run the Python script
python upload_simulation_to_storage.py "$SIMULATION" "$SIMULATION_ID" "$BUCKET"