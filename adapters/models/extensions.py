from ...utils.constants import ALLOWED_EXTENSIONS

class AllowedExtensionsModel:
  def __init__(self):
    self.__allowed_extensions = ALLOWED_EXTENSIONS

  def get_all(self):
    return self.__allowed_extensions