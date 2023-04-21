FROM ghcr.io/asreview/asreview:v1.2

# Install necessary packages and libraries
RUN apt-get update
RUN pip install exoscale~=0.7.1
RUN pip install --upgrade asreview-makita~=0.6.3
RUN pip install sentence-transformers~=2.2.2 https://github.com/jteijema/asreview-reusable-fe/archive/main.zip https://github.com/jteijema/asreview-XGBoost/archive/main.zip gensim~=4.2.0 

# Set up synergy
RUN pip install --pre --upgrade synergy-dataset
RUN mkdir -p /app/synergy
RUN synergy get -l -o ./app/synergy

# Set up the working directory and copy the script
WORKDIR /app

# Copy the simulation script into the container
COPY docker/run_simulation.sh .
COPY docker/upload_to_storage.py .
COPY docker/custom_arfi.txt.template .

# Make the script executable
RUN chmod +x run_simulation.sh
RUN chmod +x upload_to_storage.py

# Set the entrypoint and default command
ENTRYPOINT ["./run_simulation.sh"]
CMD [$DATASET, $SETTINGS, $BUCKET]
