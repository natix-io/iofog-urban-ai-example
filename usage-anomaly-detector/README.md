# usage-anomaly-detector
this usage-anomaly-detector represent an edge compute device trying to detect anomaly in each device power usage.
## Prerequisites
please build the edge-device first.
## build image
to build image run : `docker build --no-cache --tag  natix-io/usage-anomaly-detector:v1 .`
## to deploy
run `iofogctl deploy application -f config.yaml`


## hint
you can have multiple Edge Device with diffrent names just by changing microservices.name,microservices.config.tag,microservices.config.minUsage and microservices.config.maxUsage in config.yml

# release note
added restful api endpoint /api/raw
browse `http://127.0.0.1:7778/api/raw` to see AI result which change every 30 seconds by each data dispatch.