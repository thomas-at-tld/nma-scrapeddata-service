def build_mongo_query(search_string):

    if search_string == "*":
        return {}
    query = {'Name': {'$regex': f'.*{search_string}.*', '$options': 'i'}}
    return query

