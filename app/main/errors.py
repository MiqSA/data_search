from main import main
import json


@main.app_errorhandler(500)
def handle_exception_500(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": 'Error! Sorry, but an internal error occured!',
    })
    response.content_type = "application/json"
    return response


@main.app_errorhandler(404)
def handle_exception_404(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": 'Error! Try a valid endpoint!',
    })
    response.content_type = "application/json"
    return response


@main.app_errorhandler(422)
def handle_exception_422(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": 'Error! Please, check the fields required.',
    })
    response.content_type = "application/json"
    return response
