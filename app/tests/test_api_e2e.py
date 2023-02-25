from tests.conftest import client, flag_delete_rows
import json

def test_success_api(client):
    payload={
        "start_date": "1970-03-30 00:00:00", 
        "end_date": "2012-06-30 00:00:00",
        "title": "A vantagem de inovar em estado puro",
        "uri": "https://wise.org/"
        }
    response = client.post('/v1.0', json=payload)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    if not flag_delete_rows:
        assert len(response_data['results'])>1

 

def test_success_api_filter_by_title(client):
    payload={
        "title": "A arte de ",
        }
    response = client.post('/v1.0/title', json=payload)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    if not flag_delete_rows:
        assert len(response_data['results'])>1

def test_error_api_filter_by_title(client):
    payload={
        "dump": "",
        }
    response = client.post('/v1.0/title', json=payload)
    assert response.status_code == 422
  
def test_success_api_filter_by_uri(client):
    payload={
        "uri": "http://matthew",
        }
    response = client.post('/v1.0/uri', json=payload)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    if not flag_delete_rows:
        assert len(response_data['results'])>1

def test_error_api_filter_by_uri(client):
    payload={
        "dump": "",
        }
    response = client.post('/v1.0/uri', json=payload)
    assert response.status_code == 422

def test_success_api_filter_by_date_between(client):
    payload={
        "start_date": "1985-03-30 00:00:00", 
        "end_date": "2012-06-30 00:00:00",
        }
    response = client.post('/v1.0/date', json=payload)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    if not flag_delete_rows:
        assert len(response_data['results'])>1

def test_success_api_filter_by_date_after(client):
    payload={
        "start_date": "1985-03-30 00:00:00", 
        "end_date": "",
        }
    response = client.post('/v1.0/date', json=payload)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    if not flag_delete_rows:
        assert len(response_data['results'])>1

def test_success_api_filter_by_date_before(client):
    payload={
        "start_date": "", 
        "end_date": "2012-06-30 00:00:00",
        }
    response = client.post('/v1.0/date', json=payload)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    if not flag_delete_rows:
        assert len(response_data['results'])>1