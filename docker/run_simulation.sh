#!/bin/bash

# Load the dataset
# python -m synergy get $DATASET

# Run the simulation
asreview simulate $DATASET -s $SIMULATION $SETTINGS

cat << EOF > /app/exoscale/exoscale.toml
defaultaccount = "$ACCOUNT_NAME"

[[accounts]]
  account = "$ACCOUNT"
  defaultZone = "de-fra-1"
  endpoint = "https://api.exoscale.com/v1"
  environment = ""
  key = "$EXO_ACCESS_KEY_ID"
  name = "$ACCOUNT_NAME"
  secret = "$EXO_SECRET_ACCESS_KEY"
EOF

# Upload the results to the Exoscale Object Storage service
EXO_URI="sos://asreview-output/$SIMULATION_ID/$SIMULATION"
exo storage upload $SIMULATION $EXO_URI --acl public-read
