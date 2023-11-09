from application.app import create_app
from model.user import User
import pytest




@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

@pytest.fixture
def user():
    user = User("user1", "", "")
    return user