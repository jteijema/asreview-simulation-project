#!/bin/bash

# Load the dataset
# python -m synergy get $DATASET

# Run the simulation
asreview simulate $DATASET -s $SIMULATION $SETTINGS

# Upload the results to the Exoscale Object Storage service
EXO_URI="sos://asreview-output/$SIMULATION_ID/$SIMULATION"
exo storage upload $SIMULATION $EXO_URI --acl public-read
