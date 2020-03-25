# natix-iofog-ai example
this is natix-iofog-ai example bundle. here we demonstrate an urban power usage anomaly detector serving on edge.
## Prerequisites
please modify `[your-host-ip-here]` in `config.yaml` to point to your host machine.

## up and running
just execute setup.sh and in a few minutes the demo is ready.

## hint
you can have multiple Edge Device with diffrent names just by changing microservices.name,microservices.config.tag,microservices.config.minUsage and microservices.config.maxUsage in config.yml

# release note
### 1
added restful api endpoint /api/raw
browse `http://127.0.0.1:5000/api/raw` to see AI result which change every 30 seconds by each data dispatch.
### 2
added dashboard
browse `http://127.0.0.1:7778/` to see a diagram report.
