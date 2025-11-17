from app import app

# Vercel expects a handler function for serverless functions
def handler(request, response):
    with app.app_context():
        return app(request, response)

# Alternative approach that also works:
# from app import app as application
