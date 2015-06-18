from config import *


"""
TEST RESPONSES
Includes all status code responses for delete requests.
"""
  
def test_delete_no_records_returns_200_code():
  """
  SUMMARY:  Test that DELETE method returns a 200 code if no records found
  METHOD:   (1) Create a improper payload (No records).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 200.
  """
  
  # Act
  r = requests.delete('http://capstonedd.cs.pdx.edu:1337/users', data=datafquery)

  # Assert
  assert r.status_code == 200
  
  
def test_delete_returns_200_code(insert_test):
  """
  SUMMARY:  Test that proper DELETE method returns a 200 code ('ok')
  METHOD:   Send a DELETE request with proper post body.
  FAIL:     Status code is not 200.
  """
  
  # Act
  r = requests.delete('http://capstonedd.cs.pdx.edu:1337/users', data=datafquery)
  
  # Assert
  assert r.status_code == 200
    
def test_delete_deletes_record(insert_test):
  """
  SUMMARY:  Test that proper DELETE method deletes the record.
  METHOD:   Send a DELETE request with proper post body.
  FAIL:     Record has not been deleted.
  """
  
  # Act
  r = requests.delete('http://capstonedd.cs.pdx.edu:1337/users', data=datafquery)
  
  # Assert
  assert collection.count(findq) == 0
