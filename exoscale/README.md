## Generating jobs.yaml
With ASReview Makita, a jobs.yaml file can be generated to run a simulation. The jobs.yaml file contains the parameters for the simulation. The parameters can be set in the command line or in the jobs.yaml file. The jobs.yaml file can be generated with the following command:

```console
synergy get -l
asreview makita template arfi --template jobs.yaml.template -s synergy_dataset -f jobs.yaml
```