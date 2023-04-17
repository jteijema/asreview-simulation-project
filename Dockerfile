FROM ghcr.io/asreview/asreview:v1.2

# Install necessary packages and libraries
RUN apt-get update
RUN pip install exoscale~=0.7.1
# sentence-transformers~=2.2.0 gensim~=4.2.0 

# Set up synergy
RUN pip install --pre --upgrade synergy-dataset
RUN mkdir -p /app/synergy
RUN synergy get -l -o ./app/synergy

# Set up the working directory and copy the script
WORKDIR /app

# Copy the simulation script into the container
COPY docker/run_simulation.sh .
COPY docker/upload_to_storage.py .

# Make the script executable
RUN chmod +x run_simulation.sh

# Set the entrypoint and default command
ENTRYPOINT ["./run_simulation.sh"]
CMD [$DATASET, $SIMULATION_FILE, $SETTINGS, $SIMULATION_ID, $BUCKET]
