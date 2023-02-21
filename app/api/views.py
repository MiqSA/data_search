from api import api

@api.route('/')
def hello():
    return { "hello": 'Word'}