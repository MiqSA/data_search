from marshmallow import Schema, fields
from flask_apispec import doc, use_kwargs
from flask import request
from api import api
from responses import response_api
from api.controllers import Filters



class FiltersSchema(Schema):
    start_date = fields.String()
    end_date = fields.String()
    title = fields.String()
    uri = fields.String()

class DatesSchema(Schema):
    start_date = fields.String()
    end_date = fields.String()


@api.route('', methods=['POST'], provide_automatic_options=False)
@doc(description='Search data', tags=['Search'])
@use_kwargs(FiltersSchema)
def get_info(**kwargs):
    try:
        data_request = request.get_json()
        start_date = data_request.get('start_date')
        end_date = data_request.get('end_date')
        uri = data_request.get('uri').lower()
        title = data_request.get('title').lower()
        data = Filters().all(start_date, end_date, uri, title)
        return response_api(200, data)
    except Exception as err:
        print('Error in api view', err)
        return response_api(400, None)


@api.route('/date', methods=['POST'], provide_automatic_options=False)
@doc(description='Search data', tags=['Search'])
@use_kwargs(DatesSchema)
def get_info_by_date(**kwargs):
    try:
        data_request = request.get_json()
        start_date = data_request.get('start_date')
        end_date = data_request.get('end_date')
        data = Filters().by_date(start_date, end_date)
        return response_api(200, data)
    except Exception as err:
        print('Error in api view', err)
        return response_api(400, None)


@api.route('/uri', methods=['POST'], provide_automatic_options=False)
@doc(description='Search data', tags=['Search'])
@use_kwargs({'uri': fields.String()})
def get_info_by_uri(**kwargs):
    try:
        data_request = request.get_json()
        uri = data_request.get('uri')
        data = Filters().by_uri(uri.lower())
        return response_api(200, data)
    except Exception as err:
        print('Error in get info by uri', err)
        return response_api(400, None)


@api.route('/title', methods=['POST'], provide_automatic_options=False)
@doc(description='Search data', tags=['Search'])
@use_kwargs({'title': fields.String()})
def get_info_by_title(**kwargs):
    try:
        data_request = request.get_json()
        title = data_request.get('title')
        data = Filters().by_title(title.lower())
        return response_api(200, data)
    except Exception as err:
        print('Error in get info by title', err)
        return response_api(400, None)