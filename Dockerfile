FROM python:3.9-slim-buster

# Install necessary packages and libraries
RUN apt-get update
RUN pip install asreview exoscale

LABEL org.opencontainers.image.source https://github.com/jteijema/asreview-cloud-simulation-project

# Set up synergy
RUN mkdir -p /app/synergy
# COPY docker/pyodss-custom.zip /app/synergy/pyodss-custom.zip
# RUN pip install /app/synergy/pyodss-custom.zip

# Set up the working directory and copy the script
WORKDIR /app

# Copy the simulation script into the container
COPY docker/run_simulation.sh .
COPY docker/upload_simulation_to_storage.py .

# Set the entrypoint and default command
ENTRYPOINT ["./run_simulation.sh"]
CMD [$DATASET, $SIMULATION, $SETTINGS, $SIMULATION_ID, $BUCKET]
