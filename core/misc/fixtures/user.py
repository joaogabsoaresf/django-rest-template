import pytest

class MockUser:
    def __init__(self, email):
        self.email = email

@pytest.fixture
def mock_user():
    return MockUser(email="test@example.com")