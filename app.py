import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello from Flask on Kubernetes! Commit: {os.environ.get('GITHUB_SHA', 'local')}"

