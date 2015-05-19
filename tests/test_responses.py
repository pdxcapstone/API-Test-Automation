import pytest
import requests
import json

"""
TEST RESPONSES
Includes all status code responses for both get and post requests.
"""

def test_get_returns_200_code():
  """
  SUMMARY:  Test that GET method returns a 200 code ('ok')
  METHOD:   (1) Send a GET request with API credentials.
  FAIL:     Status code is not 200.
  """
  # Arrange
  payload = {'u': 'django', 'v': '123456'}
  
  # Act
  r = requests.get('http://capstonedd.cs.pdx.edu:8000/match/', params=payload)

  # Assert
  assert r.status_code == 200
  
def test_post_returns_200_code():
  """
  SUMMARY:  Test that invalid POST body returns a 200 code ('ok')
  METHOD:   (1) Send a POST request with proper post body.
  FAIL:     Status code is not 200.
  """
  # Arrange
  payload = {
    'lastName': 'Hampshire',
    'firstName': 'Aaron'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:8000/json', data=json.dumps(payload))

  # Assert
  assert r.status_code == 200
  
def test_bad_post_returns_400_code():
  """
  SUMMARY:  Test that POST method returns a 200 code ('bad request')
  METHOD:   (1) Create a improper payload (no firstName).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400.
  """
  # Arrange
  payload = {
    'lastName': 'Hampshire'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:8000/json', data=json.dumps(payload))

  # Assert
  assert r.status_code == 400