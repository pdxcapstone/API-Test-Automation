import pytest
import requests
import json

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
  FAIL:     Status code is not 200.
  """
  # Arrange
  payload = {
    'firstName' : 'Baiyu',
    'lastName' : 'Liu',
    'email' : 'baiyu@pdx.edu',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert r.status_code == 200
  
  
def test_get_param_200_code():
  """
  SUMMARY:  Test that GET method returns a 200 code ('ok')
  METHOD:   Send a GET request with required parameters.
  FAIL:     Status code is not 200.
  """
  # Arrange
  payload = {
    'firstName' : 'Baiyu',
    'lastName' : 'Liu',
    'email' : 'baiyu@pdx.edu',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.get('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))
  
  # Assert
  assert r.status_code == 200
  
def test_bad_post1_returns_400_code():
  """
  SUMMARY:  Test that invalid POST method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (same email).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400.
  """
  # Arrange
  payload = {
    'firstName' : 'Baiyu',
    'lastName' : 'Liu',
    'email' : 'baiyu@pdx.edu',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert r.status_code == 400
  
def test_bad_post2_returns_400_code():
  """
  SUMMARY:  Test that invalid POST method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (no firstName).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400.
  """
  # Arrange
  payload = {
    'lastName' : 'Liu',
    'email' : 'baiyu1@pdx.edu',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert r.status_code == 400
  
def test_bad_post3_returns_400_code():
  """
  SUMMARY:  Test that invalid POST method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (empty firstName).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400.
  """
  # Arrange
  payload = {
    'firstName' : '',
    'lastName' : 'Liu',
    'email' : 'baiyu2@pdx.edu',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert r.status_code == 400
  
def test_bad_delete_returns_400_code():
  """
  SUMMARY:  Test that invalid DELETE method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (No records).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400.
  """
  # Arrange
  payload = {
    'firstName' : 'David',
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert r.status_code == 400
  
  
def test_delete_returns_200_code():
  """
  SUMMARY:  Test that proper DELETE method returns a 200 code ('ok')
  METHOD:   Send a DELETE request with proper post body.
  FAIL:     Status code is not 400.
  """
  # Arrange
  payload = {
    'firstName' : 'Baiyu',
  }
  
  # Act
  r = requests.delete('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert r.status_code == 200
