import os
from io import BytesIO
import json

from werkzeug.utils import secure_filename
from ...utils.validators import \
  is_file_extension_allowed, is_output_format_allowed, are_valid_output_params


class ImageConvertController:
    def __init__(
      self,
      handle_image_convert,
      handle_get_allowed_input_file_extensions,
      handle_get_allowed_output_formats,
      handle_get_allowed_output_params,
      handle_get_set_output_params
    ):
        self.__convert_image = handle_image_convert

        self.__get_allowed_input_file_extensions = \
            handle_get_allowed_input_file_extensions

        self.__get_allowed_output_formats = \
            handle_get_allowed_output_formats

        self.__get_allowed_output_params = \
            handle_get_allowed_output_params

        self.__get_set_output_params = \
            handle_get_set_output_params

    def __trim_file_extension(self, file_path):
        return file_path.rsplit(".", 1)[0]

    def convert(self, app, request, jsonify):
        if "file" not in request.files:
            return jsonify({
                "status": "fail",
                "data": {"message": "No selected file or files."}
            }), 400

        upload = request.files["file"]
        file_config = request.form.get("file_config")

        if not file_config:
            return jsonify({
                "status": "fail",
                "data": {"message": "No file config found."}
            })

        try:
            file_config = json.loads(file_config)
        except Exception:
            return jsonify({
                "status": "fail",
                "data": {"message": "Unable to parse files config."}
            }), 400

        if not upload or not is_file_extension_allowed(
            upload.filename, self.__get_allowed_input_file_extensions()
        ):
            return jsonify({
                "status": "fail",
                "data": {"message": "One or more files are unsupported."}
            }), 400

        input_image = BytesIO(upload.stream.read())
        output_format = file_config["outputFormat"]
        output_params = file_config["outputParams"]

        if not is_output_format_allowed(
            output_format, self.__get_allowed_output_formats()
        ):
            return jsonify({
                "status": "fail",
                "data": {"message", "No output format or not allowed."}
            }), 400

        if not are_valid_output_params(
          output_format,
          output_params,
          self.__get_allowed_output_params(output_format)
        ):
            return jsonify({
                "status": "fail",
                "data": {
                    "message": "One or more output params are invalid."
                }
            }), 400

        output_filename = secure_filename(
            f"{self.__trim_file_extension(upload.filename)}.{output_format}"
        )

        output_path = os.path.join(
            app.config["UPLOAD_FOLDER"], output_filename
        )

        try:
            self.__convert_image(
                input_image,
                output_path,
                output_format,
                **self.__get_set_output_params(
                    output_format,
                    output_params
                )
            )
        except Exception as err:
            print(err)
            return jsonify({
                "status": "fail",
                "data":
                    {"message": "There was an error saving the images."}
            }), 500

        return jsonify({
          "status": "success",
          "data": {"convertionId": upload.filename}
        }), 200
