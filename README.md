# asreview-simulate Docker image

This Docker image provides a pre-configured environment for running the ASReview simulation tool. The image is based on the official Python 3 Docker image and includes all dependencies required for running ASReview simulations.

## Usage

To use the image, you can run it with docker run, passing any required environment variables as -e arguments. Here's an example command that runs the image with all required environment variables:

```console
docker run --rm \
  -e EXO_ACCESS_KEY_ID=<access_key> \
  -e EXO_SECRET_ACCESS_KEY=<secret_key> \
  -e ACCOUNT=<account> \
  -e ACCOUNT_NAME=<account_name> \
  -e DATASET=<dataset> \
  -e SETTINGS="<settings>" \
  -e SIMULATION=<simulation> \
  -e SIMULATION_ID=<simulation_id> \
  asreview-simulate:latest
```

Replace <access_key>, <secret_key>, <account>, <account_name>, <dataset>, <settings>, <simulation>, and <simulation_id> with the appropriate values.

The following environment variables are required:

    EXO_ACCESS_KEY_ID: the Exoscale access key ID
    EXO_SECRET_ACCESS_KEY: the Exoscale secret access key
    ACCOUNT: the Exoscale account name
    ACCOUNT_NAME: account nickname
    DATASET: the name of the dataset to use (in the form project_name:dataset_name)
    SETTINGS: the settings for the simulation
    SIMULATION: the name of the simulation to run
    SIMULATION_ID: the ID of the simulation (used to name the output directory)

## Example

Here's an example command that runs a simulation with the provided environment variables:

```console
docker run --rm \
  -e EXO_ACCESS_KEY_ID=<access_key> \
  -e EXO_SECRET_ACCESS_KEY=<secret_key> \
  -e ACCOUNT=<account> \
  -e ACCOUNT_NAME=<account_name> \
  -e DATASET=benchmark:van_de_schoot_2017 \
  -e SETTINGS="-m nb -e tfidf" \
  -e SIMULATION=test.asreview \
  -e SIMULATION_ID=test1 \
  asreview-simulate:latest
```

Replace <access_key>, <secret_key>, <account>, and <account_name> with your Exoscale access key ID, secret access key, account name, and account name, respectively.