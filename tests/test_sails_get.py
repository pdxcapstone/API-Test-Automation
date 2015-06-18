from config import *

"""
TEST RESPONSES
Includes all status code responses for get requests.
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
  
def test_get_param_200_code(insert_test):
  """
  SUMMARY:  Test that GET method returns a 200 code ('ok')
  METHOD:   Send a GET request with required parameters.
  FAIL:     Status code is not 200.
  """
  
  # Act
  r = requests.get('http://capstonedd.cs.pdx.edu:1337/users', data=datafquery)
  
  # Assert
  assert r.status_code == 200
