from main import main
from flask_apispec import doc
from flask import request
from responses import response_api


@main.route('/upload-json', methods=['POST'], provide_automatic_options=False)
@doc(description='Upload json data', tags=['menu'])
def upload_json(**kwargs):
    data = request.get_json()
    from models import Data
    from datetime import datetime
    uri = data['uri']
    title = data['title']
    date = datetime.now()

    model = Data(uri=uri, title=title, date_added=date).save()
    return response_api(200, {'msg': 'Success Add json file in database'})
    