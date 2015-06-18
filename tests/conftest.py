from config import *
  
  
@pytest.fixture(scope="function", autouse=True)
def database_clean(request):
  c = collection.count(findq)
  if c > 0:
    collection.delete_many(findq)
  def fin():
    c = collection.count(findq)
    if c > 0:
      collection.delete_many(findq)
  request.addfinalizer(fin)
  
@pytest.fixture(scope="function")
def insert_test(request):
  collection.insert_one(query)
  def fin():
    c = collection.count(findq)
    if c > 0:
      collection.delete_many(findq)
  request.addfinalizer(fin)
  
@pytest.fixture(scope="function")
def get_record_id(request):
  r = collection.find_one(query)
  return str(r['_id']);



