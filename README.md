# natix-iofog-ai example
this is natix-iofog-ai example bundle. here we demonstrate an urban power usage anomaly detector serving on edge.
## Prerequisites
please build the edge-device first.
## hint
you can have multiple Edge Device with diffrent names just by changing microservices.name,microservices.config.tag,microservices.config.minUsage and microservices.config.maxUsage in config.yml

# release note
added restful api endpoint /api/raw
browse `http://127.0.0.1:5000/api/raw` to see AI result which change every 30 seconds by each data dispatch.