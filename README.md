# Data Search
An application to search data with some filters.

## About

This a small application that allows a user to search data using several filters:
- Date range (after, before, and between)
- Title (text search, case-insensitive, full or partial matches)
- URL (full or partial matches)

## Stacks and Methods
- Methods: Test Driver Development (TDD) using Pytest.
- Test: Pytest, Postman.
- Web development: Python, Flask.
- DevOps: Docker.

## How can I use?
```
$ docker-compose up --build

# The application shoul be running in http://localhost:8082/

# To access the documentation, check in http://localhost:8082/docs

```

## Endpoints

### + Upload a json file
- *Description* = A endpoint to upload json file.
- *Name* = `/upload/json`
- *Use example*
    ```
    def test_success_upload_file(client):
        filename = 'input/data.json'
        with open(filename, 'rb') as file:
        response = client.post('/upload/json', content_type='multipart/form-data', data={'file': file})

        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == 'Success!'
    ```
### + Upload more data from request body
- *Description* = A endpoint to upload more data from request body.
- *Name* = `/upload`
- *Use example*
    ```
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
    ```


### + Search with all filters.
- *Description* = A endpoint to search in database with all filters (uri, title, start_date and end_date).
- *Name* = `/v1.0`
- *Use example*
    ```
    def test_success_api(client):
        payload={
            "start_date": "1970-03-30 00:00:00", 
            "end_date": "2012-06-30 00:00:00",
            "title": "A vantagem de inovar em estado puro",
            "uri": "https://wise.org/"
            }
        response = client.post('/v1.0', json=payload)
        assert response.status_code == 200
    ```

### + Search with date filter.
- *Description* = A endpoint to search in database with just the date filters (start_date and end_date).
- *Name* = `/v1.0/date`
- *Use example*
    ```
    def test_success_api_filter_by_date_between(client):
        payload={
            "start_date": "1985-03-30 00:00:00", 
            "end_date": "2012-06-30 00:00:00",
            }
        response = client.post('/v1.0/date', json=payload)
        assert response.status_code == 200
    ```

### + Search with title filter.
- *Description* = A endpoint to search in database with just the title filter.
- *Name* = `/v1.0/title`
- *Use example*
    ```
    def test_success_api_filter_by_title(client):
        payload={
            "title": "A arte de ",
            }
        response = client.post('/v1.0/title', json=payload)
        assert response.status_code == 200
    ```
    
### + Search with uri filter.
- *Description* = A endpoint to search in database with just the uri filter.
- *Name* = `/v1.0/uri`
- *Use example*
    ```
    def test_success_api_filter_by_uri(client):
        payload={
            "uri": "http://matthew",
            }
        response = client.post('/v1.0/uri', json=payload)
        assert response.status_code == 200
    ``` 