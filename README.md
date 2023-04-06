# asreview-simulate Docker image

This Docker image provides a pre-configured environment for running the ASReview simulation tool. The image is based on the official Python 3 Docker image and includes all dependencies required for running ASReview simulations.

## Usage

To use the image, you can run it with docker run, passing any required environment variables as -e arguments. Here's an example command that runs the image with all required environment variables:

```console
docker run --rm \
  -e EXOSCALE_API_KEY=<access_key> \
  -e EXOSCALE_API_SECRET=<secret_key> \
  -e EXOSCALE_STORAGE_ZONE=de-fra-1 \
  -e DATASET=<dataset> \
  -e SETTINGS="<settings>" \
  -e SIMULATION=<simulation_name> \
  -e SIMULATION_ID=<simulation_id> \
  asreview-simulate:latest
```

Replace <access_key>, <secret_key>, \<dataset>, \<settings>, <simulation_name>, and <simulation_id> with the appropriate values.

The following environment variables are required:

    EXOSCALE_API_KEY: the Exoscale access key ID
    EXOSCALE_API_SECRET: the Exoscale secret access key
    EXOSCALE_STORAGE_ZONE: the Exoscale storage zone (e.g., de-fra-1)
    DATASET: the name of the dataset to use (in the form project_name:dataset_name)
    SETTINGS: the settings for the simulation
    SIMULATION: the name of the simulation to run
    SIMULATION_ID: the ID of the simulation (used to name the output directory)

## Building the image
You can build the image yourself by cloning this repository and running the following command:

```console
docker build -t asreview-simulate:latest .
```

## Example

Here's an example command that runs a simulation with the provided environment variables:

```console
docker run --rm `
  -e EXOSCALE_API_KEY=<access_key> `
  -e EXOSCALE_API_SECRET=<secret_key> `
  -e EXOSCALE_STORAGE_ZONE=de-fra-1 `
  -e DATASET=benchmark:van_de_schoot_2017 `
  -e SETTINGS="-m nb -e tfidf" `
  -e SIMULATION=vds2017.asreview `
  -e SIMULATION_ID=simulation_test `
  asreview-simulate:latest
```

Replace <access_key> and <secret_key> with your Exoscale access key ID, secret access key, account name, and account name, respectively.

## License
MIT License
