from tests.conftest import client
import json
       
def test_handler_error_422(client):
    payload={
    "name": "Flask",
    "theme": "dark"}
    response = client.post('/v1.0', json=payload)

    assert response.status_code == 422
    response_data = json.loads(response.data)
    
    assert response_data["code"] == 422
    assert response_data["name"] == "Unprocessable Entity"
    assert response_data["description"] == "Error! Please, check the fields required."

def test_handler_error_404(client):
    payload={
    "name": "Flask",
    "theme": "dark"}
    response = client.post('/v1.0/error', json=payload)

    assert response.status_code == 404

    response_data = json.loads(response.data)
    assert response_data["code"] == 404
    assert response_data["description"] == 'Error! Try a valid endpoint!'
        