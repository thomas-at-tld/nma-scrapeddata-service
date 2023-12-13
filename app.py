import os, re

import logging

from flask import Flask, request, jsonify, Blueprint
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient, TEXT
from datetime import datetime

from nmautils import build_mongo_query

app = Flask(__name__)
api_blueprint = Blueprint('api', __name__, url_prefix='/nma/scrapedData')
api = Api(api_blueprint)

# Get MongoDB credentials from environment variables
mongo_host = os.environ.get('MONGO_HOST')
mongo_username = os.environ.get('MONGO_USERNAME')
mongo_password = os.environ.get('MONGO_PASSWORD')

# Connect to MongoDB
client = MongoClient(f'mongodb://{mongo_username}:{mongo_password}@{mongo_host}:27017/')
db = client['nma-scraped-data']

class GetAllStatisticsCollections(Resource):
    def get(self):
        try:
            statistics_collections = get_statistics_collections()
            content_map = get_collection_content(statistics_collections)

            # collection_name date pattern =  '<source>-statistics-2021-05-31-15-00-00'
            sorted_collections = sorted(content_map.items(), key=lambda x: extract_date(x[0]), reverse=True)

            return jsonify(sorted_collections)

        except Exception as e:
            return {'Failed to get columns for collection, Error': str(e)}, 500

def extract_date(collection_name):
    pattern = re.compile(r'\d{8}-\d{6}')
    date_tag = pattern.search(collection_name).group()
    return datetime.strptime(date_tag, '%Y%m%d-%H%M%S')


def get_statistics_collections():
    all_collections = db.list_collection_names()
    statistics_collections = [collection for collection in all_collections if "statistics" in collection.lower()]
    return statistics_collections


def get_collection_content(statistics_collections):
        content_map = {}

        for collection_name in statistics_collections:
            collection = db[collection_name]
            collection_content = list(collection.find())
            for item in collection_content:
                item['_id'] = str(item['_id'])  # Convert ObjectId to string
            # sort by field page as first priority and then by field time as second priority
            collection_content.sort(key=lambda x: x['time'], reverse=True)
            content_map[collection_name] = collection_content

        return content_map


api.add_resource(GetAllStatisticsCollections, '/statistics')

# Register the Blueprint with the Flask app
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(port=6000, debug=True)