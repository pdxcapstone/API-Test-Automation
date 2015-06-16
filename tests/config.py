import pytest
import requests
import json
from pymongo import MongoClient


"""
Basic Queries
"""

query = {
    'firstName' : 'test_use',
    'lastName' : 'test01',
    'email' : 'test@capstonedd.com',
    'type' : 'buyer'
  }
  
findq = {
    'firstName' : 'test_use'
  }
  
dataquery = json.dumps(query)
datafquery = json.dumps(findq)

"""
Connect to MongoDB
"""

client = MongoClient('capstonedd.cs.pdx.edu', 27017)
# Uncomment this line if you have auth options
# client = MongoClient('mongodb://admin:teamG@capstonedd.cs.pdx.edu')
collection = client.test.users
