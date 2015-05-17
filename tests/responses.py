import pytest
import requests

def test_api_call_returns_200_code():
  # Arrange
  payload = {'u': 'django', 'v': '123456'}
  
  # Act
  r = requests.get('http://capstonedd.cs.pdx.edu:8000/match/', params=payload)

  # Assert
  assert r.status_code == 200