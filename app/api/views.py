from api import api
import marshmallow as ma
from marshmallow import Schema, fields
from flask_apispec import ResourceMeta, Ref, doc, marshal_with, use_kwargs
from responses import response_api
from flask import request


class FiltersSchema(Schema):
    date = fields.List(fields.String())
    title = fields.String()
    url = fields.String()


@api.route('/', methods=['POST'], provide_automatic_options=False)
@doc(description='Search data', tags=['api'])
@use_kwargs(FiltersSchema)
def hello(**kwargs):
    try:
        name = kwargs.get('name', 'hello')
        data = {name: 'world!'}
        return response_api(200, data)
    except Exception as err:
        print('Error', err)
        return response_api(400, None)

    