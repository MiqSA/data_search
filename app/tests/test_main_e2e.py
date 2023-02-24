from tests.conftest import client
import json
import os

def test_success_upload_informations(client):
    payload={
        "title": "A arte de atingir seus objetivos simplesmente",
        "uri": "http://matthews-espinoza.com/",
        "date": "2014-03-08T15"
      }
    response = client.post('/upload', json=payload)

    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['message'] == 'Success!'
    assert response_data['results'][0] == 'Add informations in database with success!'


def test_success_upload_file(client):
    filename = 'input/data.json'
    with open(filename, 'rb') as file:
      response = client.post('/upload/json', content_type='multipart/form-data', data={'file': file})

    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['message'] == 'Success!'
