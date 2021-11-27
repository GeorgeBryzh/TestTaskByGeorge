import pytest
pytest_args = [
    '--junitxml=C:\\Users\\vorta\\Documents\\selenium-poshta\\AllTestResult.xml',
    'prefunc1.py',
    'prefunc2.py',
    'prefunc3.py'
    
    
]
pytest.main(pytest_args)