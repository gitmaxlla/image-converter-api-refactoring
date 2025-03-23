import os

from flask import Flask, request, jsonify

from .utils.constants import MAX_FILE_SIZE_BYTES, UPLOAD_FOLDER

from .routes.convert import image_convert_controller
from .routes.allowed_io import allowed_IO_controller
from .routes.output_format_params import output_params_controller


def create_app(upload_folder=UPLOAD_FOLDER):
    if not os.path.exists(upload_folder):
        os.mkdir(upload_folder)

    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = upload_folder
    app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE_BYTES

    @app.route("/")
    def status():
        return jsonify({"status": "success"})

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
        return image_convert_controller.convert(
            app,
            request,
            jsonify
        )

    @app.after_request
    def prevent_response_caching(response):
        response.headers["Cache-Control"] = ("no-cache,"
                                             "no-store,"
                                             "must-revalidate")
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

    return app
