class AllowedIOController:
    def __init__(self, handleGetAllowedIO):
      self.__get_allowed_IO = handleGetAllowedIO
    
    def get_io_params(self, jsonify):
       return jsonify(self.__get_allowed_IO()), 200