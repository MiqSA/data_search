from main import main
from flask_apispec import doc, use_kwargs
from marshmallow import Schema, fields
from flask import request
from responses import response_api
from main.controllers import CheckAndSave
import json

class UploadSchema(Schema):
    date = fields.String()
    title = fields.String()
    uri = fields.String()


@main.route('/upload/json', methods=['POST'], provide_automatic_options=False)
@doc(description='Upload data from json file', tags=['Uploads'])
def upload(**kwargs):
    try:
        file = request.files['file']
        all_data = json.load(file)
        for data in all_data['items']:
            CheckAndSave(data).main()
        return response_api(200, 'Add data from json in database with success!')
    except Exception as err:
        print('Error in upload', err)
        return response_api(400, None)


@main.route('/upload', methods=['POST'], provide_automatic_options=False)
@doc(description='Upload data from a body request', tags=['Uploads'])
@use_kwargs(UploadSchema)
def upload_informations(**kwargs):
    try:
        data = request.get_json()
        CheckAndSave(data).main()
        return response_api(200, 'Add informations in database with success!')
    except Exception as err:
        print('Error in upload_informations', err)
        return response_api(400, None)