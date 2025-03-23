class AllowedIOController:
    def __init__(self, handle_get_allowed_IO):
        self.__get_allowed_IO = handle_get_allowed_IO

    def get_io_params(self, jsonify):
        return jsonify(self.__get_allowed_IO()), 200
