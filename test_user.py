import pytest
import flask
import json
from model.user import User


from conftest import client, user


def test_health_status_code_ok(client):
	response = client.get('/health')
	assert response.status_code == 200

def test_health_message(client):
	response = client.get('/health')
	data = response.data.decode() #Decodes the request data
	assert data == 'System is Up'
	
def test_get_user_details(client, user):
	response = client.get('/users/' + user.id)
	data = response.data.decode() #Decodes the request data
	j = json.loads(data)
	assert j["status"] == 200
	uj = json.loads(j["user"])
	u = User(**uj)
	assert u.first_name == "john1"



