from PIL import Image

from ..adapters.models.image import ImageConvertModel
from ..usecases.convert_image import convert_image

from ..adapters.models.io import AllowedInputFileExtensionsModel
from ..usecases.get_allowed_input_file_extensions import \
  get_allowed_input_file_extensions

from ..adapters.controllers.image import ImageConvertController

image_model = ImageConvertModel(Image)
handle_image_convert = convert_image(image_model)

allowed_input_file_extensions_model = AllowedInputFileExtensionsModel()
handle_get_allowed_input_file_extensions = \
  get_allowed_input_file_extensions(allowed_input_file_extensions_model)

image_controller = ImageConvertController(
  handle_image_convert,
  handle_get_allowed_input_file_extensions
)