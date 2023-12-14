# nma-scrapeddata-service
Provides an API to fetch information from database holding scraped data.

# Python packages needed
pip install Flask flask-restful pymongo

# Build docker image for local docker container
docker build --build-arg MONGO_HOST=host.docker.internal --build-arg MONGO_USERNAME=admin --build-arg MONGO_PASSWORD=nmaMongoPw -t nma-scrapeddata-service .

# Build docker image for aws testing
docker build --build-arg MONGO_HOST=ec2-51-20-253-180.eu-north-1.compute.amazonaws.com --build-arg MONGO_USERNAME=admin --build-arg MONGO_PASSWORD=2m2oA5Bd3aTjqar3 -t nma-scrapeddata-service .

# Start docker container
docker run -p6000:6000 --net nma-microservices --add-host=host.docker.internal:host-gateway --name nma-scrapeddata-service nma-scrapeddata-service:latest

# Run application from command line and interact with local mongodb
export MONGO_HOST=localhost
export MONGO_USERNAME=admin
export MONGO_PASSWORD=nmaMongoPw
python3 app.py

# Run application from command line and interact with aws mongodb
export MONGO_HOST=ec2-51-20-253-180.eu-north-1.compute.amazonaws.com
export MONGO_USERNAME=admin
export MONGO_PASSWORD=2m2oA5Bd3aTjqar3
python3 app.py

# Search API / example

# Get all collections containing "statitics" in the collection name (sorted on date/time in collection name)  
curl http://localhost:5000/nma/scrapedData/statistics



