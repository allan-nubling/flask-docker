from model import categorie_prediction as cp
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/predict', methods=['POST'])
def test():
    return {
        'prediction': cp(request.get_json()["texts_snippets"])
    }
