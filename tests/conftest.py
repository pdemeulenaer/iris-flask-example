import pytest
from app import app


@pytest.fixture(scope="session")
def client():
    '''
    This fixture creates the client Flask app that will be used in all Flask tests
    '''
    return app.test_client()
