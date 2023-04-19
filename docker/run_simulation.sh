#!/bin/bash

# Load the dataset
# python -m synergy get $DATASET

# Grabbing the dataset
mkdir -p data
cp "synergy/$DATASET.csv" "data/$DATASET.csv"

# Makita
echo -e "\nGenerating Makita Template with settings: $SETTINGS and dataset: $DATASET\n"
asreview makita template arfi --template custom_arfi.txt.template -s data -f job.sh
echo -e "job.sh generated: "
cat job.sh

# Run the simulation
echo -e "Running simulation for dataset $DATASET with settings $SETTINGS\n"
chmod +x job.sh
./job.sh "$@"