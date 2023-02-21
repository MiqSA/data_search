from main import main

@main.route('/')
def home():
    return {
        'Explore data':'/v1.0/',
        'Swagger': '/docs/' 
    }