from app import app
from vercel_py import serve

handler = serve(app)
