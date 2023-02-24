from marshmallow import Schema, fields
from flask_apispec import doc, use_kwargs
from flask import request
from api import api
from responses import response_api



class FiltersSchema(Schema):
    date = fields.List(fields.String())
    title = fields.String()
    uri = fields.String()


@api.route('/', methods=['POST'], provide_automatic_options=False)
@doc(description='Search data', tags=['Search'])
@use_kwargs(FiltersSchema)
def get_info(**kwargs):
    try:
        return response_api(200, {'msg': 'Success Add json file in database'})
    except Exception as err:
        print('Error in api view', err)
        return response_api(400, None)
