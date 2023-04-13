#!/bin/bash

# Load the dataset
# python -m synergy get $DATASET

# prints
echo "Running simulation..."
echo "DATASET: $DATASET"
echo "SETTINGS: $SETTINGS"
echo "SIMULATION_FILE: $SIMULATION_FILE"
echo "SIMULATION_ID: $SIMULATION_ID"

# Run the simulation
asreview simulate ./synergy/$DATASET.csv -s $SIMULATION_FILE $SETTINGS
asreview metrics $SIMULATION_FILE -o $SIMULATION_FILE.json

# Run the Python script
python upload_to_storage.py "$SIMULATION_FILE" "$SIMULATION_ID" "$BUCKET"
python upload_to_storage.py "$SIMULATION_FILE.json" "$SIMULATION_ID" "$BUCKET"