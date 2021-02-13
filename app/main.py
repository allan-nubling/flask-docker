from waitress import serve
import os
from app import app
PORT = os.environ['PORT']
serve(app, host="0.0.0.0", port=PORT)
