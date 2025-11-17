from app import app

def handler(request, response):
    with app.app_context():
        return app(request, response)
