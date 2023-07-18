#!/usr/bin/env python3
""" 12-log_stats.py """

from pymongo import MongoClient

def get_logs_count(mongo_collection):
    return mongo_collection.count_documents({})

def get_methods_count(mongo_collection):
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    return method_counts

def get_status_check_count(mongo_collection):
    return mongo_collection.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    logs_count = get_logs_count(logs_collection)
    print("{} logs".format(logs_count))

    print("Methods:")
    method_counts = get_methods_count(logs_collection)
    for method, count in method_counts.items():
        print("    method {}: {}".format(method, count))

    status_check_count = get_status_check_count(logs_collection)
    print("{} status check".format(status_check_count))
