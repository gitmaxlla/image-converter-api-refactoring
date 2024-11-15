import os

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from .routes.convert import image_controller
from .routes.allowed_extensions import allowed_extensions_controller

UPLOAD_FOLDER = "./uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def status():
    return jsonify({ "status": "success" })


@app.route("/allowed-extensions", methods=["GET"])
def allowed_extensions():
    return allowed_extensions_controller.get_all(
        jsonify
    )


@app.route("/convert", methods=["POST"])
def convert():
    return image_controller.convert(
        app,
        request,
        secure_filename,
        jsonify
    )