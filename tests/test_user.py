import pytest
import flask


from conftest import client


def test_health_status_code_ok(client):
	response = client.get('/health')
	assert response.status_code == 200

def test_health_message(client):
	response = client.get('/health')
	data = response.data.decode() #Decodes the request data
	assert data == 'System is Up'