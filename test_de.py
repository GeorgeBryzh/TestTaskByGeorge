import pytest
@pytest.hookimpl(trylast=True)
def d():
  assert 1==1

 

