from config import *


"""
TEST RESPONSES
Includes all status code responses for put requests.
"""
  
def test_put_returns_200_code(insert_test, get_record_id):
  """
  SUMMARY:  Test that proper PUT method update the record.
  METHOD:   Send a PUT request with proper post body.
  FAIL:     Status code is not 200.
  """
  
  # Arrange
  payload = {
    'id' : get_record_id,
    'email' : 'modified@example.com'
  }
  
  # Act
  r = requests.put('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))
  
  # Assert
  assert r.status_code == 200
  

def test_put_modifies_record(insert_test, get_record_id):
  """
  SUMMARY:  Test that proper PUT method update the record.
  METHOD:   Send a PUT request with proper post body.
  FAIL:     Email is not correctly modified.
  """
  
  # Arrange
  payload = {
    'id' : get_record_id,
    'email' : 'modified@example.com'
  }
  
  # Act
  r = requests.put('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))
  
  # Assert
  assert collection.find_one(findq)['email'] == 'modified@example.com'
  
def test_put_returns_400_code(insert_test):
  """
  SUMMARY:  Test that invalid PUT method gets 400 code ("Bad Request").
  METHOD:   Send a PUT request with proper post body.
  FAIL:     Status code is not 400.
  """
  
  # Arrange
  payload = {
    'email' : 'modified@example.com'
  }
  
  # Act
  r = requests.put('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))
  
  # Assert
  assert r.status_code == 400
  
def test_put_returns_error_message1(insert_test):
  """
  SUMMARY:  Test that invalid PUT method gets error message.
  METHOD:   Send a PUT request with proper post body.
  FAIL:     Error message is not correct.
  """
  
  # Arrange
  payload = {
    'email' : 'modified@example.com'
  }
  
  # Act
  r = requests.put('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))
  
  # Assert
  assert r.json()['error'] == 'no id provided.'
  
  
def test_put_returns_404_code(insert_test):
  """
  SUMMARY:  Test that invalid PUT method gets 404 code ("Not Found").
  METHOD:   Send a PUT request with proper post body.
  FAIL:     Status code is not 404.
  """
  
  # Arrange
  payload = {
    'id' : 'invalid',
    'email' : 'modified@example.com'
  }
  
  # Act
  r = requests.put('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))
  
  # Assert
  assert r.status_code == 404
  
def test_put_returns_error_message2(insert_test):
  """
  SUMMARY:  Test that invalid PUT method gets error message.
  METHOD:   Send a PUT request with proper post body.
  FAIL:     Error message is not correct.
  """
  
  # Arrange
  payload = {
    'id' : 'invalid',
    'email' : 'modified@example.com'
  }
  
  # Act
  r = requests.put('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))
  
  # Assert
  assert r.json()['error'] == 'User not found.'
