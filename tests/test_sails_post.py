from config import *


"""
TEST RESPONSES
Includes all status code responses for post requests.
"""

def test_post_returns_200_code():
  """
  SUMMARY:  Test that valid POST body returns a 200 code ('ok')
  METHOD:   Send a POST request with proper post body.
  FAIL:     Status code is not 200.
  """
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=dataquery)

  # Assert
  assert r.status_code == 200
    
def test_post_inserts_record():
  """
  SUMMARY:  Test that valid POST body returns a 200 code ('ok')
  METHOD:   Send a POST request with proper post body.
  FAIL:     Nothing has been inserted.
  """
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=dataquery)

  # Assert
  assert collection.count(findq) == 1
  
  
def test_bad_post1_returns_400_code(insert_test):
  """
  SUMMARY:  Test that invalid POST method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (same email).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400.
  """
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=dataquery)

  # Assert
  assert r.status_code == 400
    
def test_bad_post1_fails_insertion(insert_test):
  """
  SUMMARY:  Test that invalid POST method doesn't insert.
  METHOD:   (1) Create a improper payload (same email).
            (2) Send a POST request with improper post body.
  FAIL:     Number of test01 record is not 1.
  """
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=dataquery)

  # Assert
  assert collection.count(findq) == 1
  
def test_bad_post2_returns_400_code():
  """
  SUMMARY:  Test that invalid POST method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (no firstName).
            (2) Send a POST request with improper post body.
  FAIL:     Status code is not 400.
  """
  
  # Arrange
  payload = {
    'lastName' : 'test01',
    'email' : 'test@pdxcapstone.com',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert r.status_code == 400
    
def test_bad_post2_fails_insertion():
  """
  SUMMARY:  Test that invalid POST method doesn't insert.
  METHOD:   (1) Create a improper payload (no firstName).
            (2) Send a POST request with improper post body.
  FAIL:     Number of test01 record is not 0.
  """
  
  # Arrange
  payload = {
    'lastName' : 'test01',
    'email' : 'test@pdxcapstone.com',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert collection.count(findq) == 0
  
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
    'lastName' : 'test01',
    'email' : 'test@pdxcapstone.com',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert r.status_code == 400
    
def test_bad_post3_fails_insertion():
  """
  SUMMARY:  Test that invalid POST method returns a 400 code ('bad request')
  METHOD:   (1) Create a improper payload (empty firstName).
            (2) Send a POST request with improper post body.
  FAIL:     Number of test01 is not zero.
  """

  # Arrange
  payload = {
    'firstName' : '',
    'lastName' : 'test01',
    'email' : 'test@pdxcapstone.com',
    'type' : 'buyer'
  }
  
  # Act
  r = requests.post('http://capstonedd.cs.pdx.edu:1337/users', data=json.dumps(payload))

  # Assert
  assert collection.count(findq) == 0
  
