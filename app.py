import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(
        message="Hello from Kubernetes",
        pod=socket.gethostname(),
        version=os.getenv("APP_VERSION", "dev"),
    )

@app.route("/health")
def health():
    return jsonify(status="ok"), 200