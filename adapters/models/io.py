from ...utils.constants import ALLOWED_IO

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