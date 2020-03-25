#!/bin/bash
docker build --no-cache -t natix-io/edge-device:v1 -f ./edge-device/Dockerfile .
docker build --no-cache -t natix-io/usage-anomaly-detector:v1 -f ./usage-anomaly-detector/Dockerfile .
docker build --no-cache -t natix-io/usage-anomaly-dashboard:v1 -f ./usage-anomaly-dashboard/Dockerfile .
iofogctl deploy -f quick-start.yaml 
echo "waiting for iofog agent ..."
sleep 10
iofogctl deploy -f config.yaml