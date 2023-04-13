## Generating jobs.yaml
With ASReview Makita, a jobs.yaml file can be generated that can be used to run a simulation. The jobs.yaml file contains the parameters for the simulation. The jobs.yaml file can be generated with the following command:

```console
synergy get -l
asreview makita template arfi --template jobs.yaml.template -s synergy_dataset -f jobs.yaml
```

It is based on the Makita template `jobs.yaml.template` which is a custom template dependend on the ARFI template.
