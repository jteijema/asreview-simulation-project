# ASReview Simulation Project 

This repository contains the code and supporting files for the ASReview simulation project. It is primarily intended for use with the paper (provide paper reference here) and offers a comprehensive package for running ASReview simulations, launching the cluster, and analyzing the results.

The project is composed of three main components:

- The ASReview-simulate Docker image
- Exoscale cluster launch scripts
- Output analysis scripts

## ASReview-Simulate Docker Image

The Docker image provides a pre-configured environment for running the ASReview simulation tool. The image is based on the official Python 3 Docker image and includes all dependencies required for running ASReview simulations.

The image uses the [Synergy dataset](https://github.com/asreview/synergy-dataset-py), and will run the ARFI template for a single dataset using [Makita](https://github.com/asreview/asreview-makita).

### Usage

To pull the image from GitHub Container Registry, run the following command:

\```console
docker pull ghcr.io/jteijema/asreview-simulation-project:latest
docker tag ghcr.io/jteijema/asreview-simulation-project:latest asreview-simulate
\```

### Running the Docker Image

To use the image, run it with `docker run`, passing any required environment variables as `-e` arguments. For example:

\```console
docker run --rm \
  -e EXOSCALE_API_KEY=<access_key> \
  -e EXOSCALE_API_SECRET=<secret_key> \
  -e EXOSCALE_STORAGE_ZONE=de-fra-1 \
  -e BUCKET=<bucket_name> \
  -e DATASET=<dataset> \
  -e SETTINGS="<settings>" \
  asreview-simulate
\```

Replace \<variable> with the appropriate values.

### Environment Variables

The following environment variables are required:

- `EXOSCALE_API_KEY`: the Exoscale access key ID
- `EXOSCALE_API_SECRET`: the Exoscale secret access key
- `EXOSCALE_STORAGE_ZONE`: the Exoscale storage zone (e.g., de-fra-1)
- `BUCKET`: the name of the Exoscale bucket to use
- `DATASET`: the name of the dataset to use from synergy
- `SETTINGS`: the settings for the simulation

### Building the Docker Image

You can build the image yourself by cloning this repository and running the following command:

\```console
docker build -t asreview-simulate:latest .
\```

## Exoscale

The `exoscale` folder contains scripts for launching the cluster on Exoscale.

## Output

The `output` folder contains scripts for analyzing the results of a simulation study.

## Example

Here's an example command that runs a simulation with the provided environment variables:

\```console
docker run --rm \
  -e EXOSCALE_API_KEY=<access_key> \
  -e EXOSCALE_API_SECRET=<secret_key> \
  -e EXOSCALE_STORAGE_ZONE=de-fra-1 \
  -e BUCKET=asreview-output \
  -e DATASET=Donners_2021 \
  -e SETTINGS="-m nb -e tfidf" \
  asreview-simulate
\```

Replace <access_key> and <secret_key> with your Exoscale access key ID, secret access key, and account name, respectively.

## Results
An example of the results of the simulation can be found on [the simulation website.](https://jteijema.github.io/synergy-simulations-website/).
For these results, the docker image was ran 338 times.

## License

This project is licensed under the terms of the Attribution 4.0 International (CC BY 4.0). See the LICENSE.md file for details.
