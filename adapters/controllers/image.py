import os
from io import BytesIO

from ...utils.constants import WEBP, ALLOWED_EXTENSIONS
from ...utils.functions import is_file_extension_allowed

OUTPUT_FORMAT = WEBP
DEFAULT_QUALITY = 95

class ImageConvertController:
    def __init__(self, handle_image_convert):
        self.__convert_image = handle_image_convert
    
    def convert(self, app, request, secure_filename, jsonify):
        if "file" not in request.files:
          return jsonify({
              "status": "fail",
              "data": { "message": "No selected file or files." }
          }), 400
    
        files = request.files.getlist("file")

        for file in files:
            if not file or not is_file_extension_allowed(
                file.filename, ALLOWED_EXTENSIONS
            ):
                return jsonify({
                    "status": "fail",
                    "data": { "message": "One or more files are unsupported." }
                }), 400
            
            input_image = BytesIO(file.stream.read())
            output_filename = secure_filename(
                f"{file.filename.rsplit(".", 1)[0]}.{OUTPUT_FORMAT}"
            )
            output_path = os.path.join(
                app.config["UPLOAD_FOLDER"], output_filename
            )

            try:
                self.__convert_image(
                    input_image,
                    output_path,
                    OUTPUT_FORMAT,
                    quality = DEFAULT_QUALITY
                )
            except Exception as err:
                print(err)
                return jsonify({
                    "status": "fail",
                    "data":
                        { "message": "There was an error saving the images."}
                }), 500

        return jsonify({"status" : "success"}), 200
        