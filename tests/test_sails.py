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
  
testq = {
    'lastName' : 'test02'
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
# Test if test record exists
c = collection.count(findq)
if c > 0:
  collection.delete_many(findq)


"""
TEST RESPONSES
Includes all status code responses for both get and post requests.
"""

def test_get_no_param_200_code():
  """
  SUMMARY:  Test that GET method returns a 200 code ('ok')
  METHOD:   Send a GET request with no parameteres.
  FAIL:     Status code is not 200.
  """
  
  # Act
  r = requests.get('http://capstonedd.cs.pdx.edu:1337/users')

  # Assert
  assert r.status_code == 200
  
  
def test_post_returns_200_code():
  """
  SUMMARY:  Test that valid POST body returns a 200 code ('ok')
  METHOD:   Send a POST request with proper post body.
  FAIL:     Status code is not 200 or nothing has been inserted.
  """
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=dataquery)

  # Assert & redo
  c = collection.count(findq)
  if c > 0:
    collection.delete_many(findq)
    assert r.status_code == 200
  else:
    raise AssertionError
  
  
def test_get_param_200_code():
  """
  SUMMARY:  Test that GET method returns a 200 code ('ok')
  METHOD:   Send a GET request with required parameters.
  FAIL:     Status code is not 200.
  """
  
  # Add record
  collection.insert_one(query)
  
  # Act
  r = requests.get('http://capstonedd.cs.pdx.edu:1337/users', data=datafquery)
  
  # Assert
  assert r.status_code == 200
  
  # Redo
  c = collection.count(findq)
  if c > 0:
    collection.delete_many(findq)
  
def test_bad_post1_returns_400_code():
  """
  SUMMARY:  Test that invalid POST method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (same email).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400 or the number of test01 is not 1.
  """
  # Add record
  collection.insert_one(query)
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=dataquery)

  # Assert and redo
  c = collection.count(findq)
  if c == 1:
    collection.delete_one(findq)
    assert r.status_code == 400
  else:
    if c > 1:
      collection.delete_many(findq)
    raise AssertionError
  
def test_bad_post2_returns_400_code():
  """
  SUMMARY:  Test that invalid POST method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (no firstName).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400 or number of test02 is not zero.
  """
  # Clean
  c = collection.count(testq)
  if c > 0:
    collection.delete_many(testq)
  
  # Arrange
  payload = {
    'lastName' : 'test02',
    'email' : 'test02@pdxcapstone.com',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  c = collection.count(testq)
  if c > 0:
    collection.delete_many(testq)
    raise AssertionError
  else:
    assert r.status_code == 400
  
def test_bad_post3_returns_400_code():
  """
  SUMMARY:  Test that invalid POST method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (empty firstName).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400 or number of test02 is not zero.
  """
  
  # Clean
  c = collection.count(testq)
  if c > 0:
    collection.delete_many(testq)  

  # Arrange
  payload = {
    'firstName' : '',
    'lastName' : 'test02',
    'email' : 'test02@pdxcapstone.com',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  c = collection.count(testq)
  if c > 0:
    collection.delete_many(testq)
    raise AssertionError
  else:
    assert r.status_code == 400
  
def test_bad_delete_returns_400_code():
  """
  SUMMARY:  Test that invalid DELETE method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (No records).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400.
  """
  
  # Clean
  c = collection.count(testq)
  if c > 0:
    collection.delete_many(testq)
  
  # Arrange
  payload = {
    'lastName' : 'test02',
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert r.status_code == 400
  
  
def test_delete_returns_200_code():
  """
  SUMMARY:  Test that proper DELETE method returns a 200 code ('ok')
  METHOD:   Send a DELETE request with proper post body.
  FAIL:     Status code is not 200 or the record has not been deleted.
  """
  
  # Add record
  collection.insert_one(query)
  
  # Act
  r = requests.delete('http://capstonedd.cs.pdx.edu:1337/users', data=datafquery)
  
  # Assert
  c = collection.count(findq)
  if c > 0:
    collection.delete_many(findq)
    raise AssertionError
  else:
    assert r.status_code == 200
