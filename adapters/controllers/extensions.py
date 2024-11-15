class AllowedExtensionsController:
    def __init__(self, handleGetAllowedExtensions):
      self.__get_allowed_extensions = handleGetAllowedExtensions
    
    def get_all(self, jsonify):
       return jsonify({
            "allowed_extensions": list(self.__get_allowed_extensions())
        }), 200