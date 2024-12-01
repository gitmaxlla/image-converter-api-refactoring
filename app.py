import os

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from .utils.constants import MAX_FILE_SIZE_BYTES

from .routes.convert import image_controller
from .routes.allowed_io import allowed_IO_controller
from .routes.output_format_params import output_params_controller

UPLOAD_FOLDER = "./uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE_BYTES

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def status():
    return jsonify({ "status": "success" })


@app.route("/allowed-io-params", methods=["GET"])
def allowed_io():
    return allowed_IO_controller.get_io_params(
        jsonify
    )


@app.route("/output-format-params", methods=["POST"])
def output_format_params():
    return output_params_controller.get_format_params(
        request,
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