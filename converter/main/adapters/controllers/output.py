class OutputParamsController:
    def __init__(self, handle_get_format_params):
        self.__get_format_params = handle_get_format_params

    def get_format_params(self, request, jsonify):
        output_format = request.form.get("output_format")

        if not output_format or len(output_format) == 0:
            return jsonify({
                "status": "fail",
                "data": { "message": "No output format specified." }
            }), 400
        
        try:
            params = self.__get_format_params(output_format)
            return jsonify({
                "status": "success",
                "data": {
                    "output_params": params
                }
            }), 200
        except KeyError as err:
            print(f"Invalid format name:{err}")
            return jsonify({
                "status": "fail",
                "data": {
                    "message": "Invalid format name."
                }
            }), 400