import pytest
from app import app


@pytest.fixture(scope="session")
def client():
    return app.test_client()