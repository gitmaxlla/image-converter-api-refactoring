from ...utils.constants import ALLOWED_IO, FORMAT_PARAMS

class AllowedIOModel:
  def __init__(self):
    self.__allowed_IO = ALLOWED_IO

  def get_io_params(self):
    return self.__allowed_IO

class AllowedInputFileExtensionsModel:
  def __init__(self):
    self.__allowed_extensions = ALLOWED_IO["input"]["file_extensions"]

  def get_all(self):
    return self.__allowed_extensions
  
class AllowedOutputFormatsModel:
  def __init__(self):
    self.__allowed_output_formats = ALLOWED_IO["output"]["file_formats"]

  def get_all(self):
    return self.__allowed_output_formats
  
class AllowedOutputParamsModel:
  def __init__(self):
    self.__format_items = FORMAT_PARAMS

  def get_format_params(self, output_format):
    items = self.__format_items[output_format]
    allowed_output_params = []

    for item in items:
      allowed_output_params.append(item["name"])

    return allowed_output_params
  
class FormatOutputParamsModel:
    def __init__(self):
        self.__format_items = FORMAT_PARAMS

    def get_formatted_output_params(self, output_format, output_params):
        items = self.__format_items[output_format]
        formatted_output_params = dict()

        for paramName in output_params:
            for item in items:
                if item.get("name") == paramName and item.get("is_bool") == 1:
                    if output_params[paramName] == 1:
                      formatted_output_params[paramName] = \
                        bool(output_params[paramName])
                elif item.get("name") == paramName \
                    and isinstance(item.get("options"), list):
                        formatted_output_params[paramName] = \
                          [tuple(output_params[paramName])]
                elif item.get("name") == paramName:
                    formatted_output_params[paramName] = \
                      output_params[paramName]
                  
        return formatted_output_params