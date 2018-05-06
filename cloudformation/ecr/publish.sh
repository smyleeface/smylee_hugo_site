#!/usr/bin/env bash

echo "*** INFO: logging in to ecr" && \
eval $(aws --profile ${profile} --region ${region} ecr get-login --no-include-email)

echo "*** INFO: building docker image" && \
docker build -t ${buildContainerName} -f ../Dockerfile.build ../

echo "*** INFO: tagging docker image" && \
docker tag ${buildContainerName}:latest ${buildContainerUrl}

echo "*** INFO: pushing docker image" && \
docker push ${buildContainerUrl}