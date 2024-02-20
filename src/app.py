from flask import Flask, jsonify, render_template
import socket
from helpers import get_host_name, get_host_ip

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health")
def health():
    return jsonify(
        status="UP&Working"
    )


@app.route("/details")
def details():
    return render_template(
        "index.html",
        host_name=get_host_name(),
        host_ip=get_host_ip()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
