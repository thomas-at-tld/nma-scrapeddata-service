#!/bin/bash

imageName="nma-scrapeddata-service"
mongoHost="ec2-13-50-237-26.eu-north-1.compute.amazonaws.com"
mongoUser="admin"
mongoPw="2m2oA5Bd3aTjqar3"
imageBuildCommand="build -t $imageName --build-arg MONGO_HOST=$mongoHost --build-arg MONGO_USERNAME=$mongoUser --build-arg MONGO_PASSWORD=$mongoPw ."

# Build image, tag and push to aws
source ../scripts/pushToAws.sh "$imageName" "$imageBuildCommand"
