from tests.conftest import client
import json

       
def test_success_api(client):
    payload={
        "date": [
            "date_0", "date_1"
        ],
        "title": "My title",
        "uri": "My URL"
        }
    response = client.post('/v1.0/', json=payload)

    assert response.status_code == 200

    response_data = json.loads(response.data)
 