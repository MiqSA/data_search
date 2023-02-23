from tests.conftest import client
import json
       

def test_success_upload_json(client):
    payload={
        "title": "A arte de atingir seus objetivos simplesmente",
        "uri": "http://matthews-espinoza.com/",
        "date": "2014-03-08T15"
      }
    response = client.post('/upload-json', json=payload)

    assert response.status_code == 200

    response_data = json.loads(response.data)