from PIL import Image

from ..adapters.models.image import ImageConvertModel
from ..usecases.convert_image import convert_image

from ..adapters.models.extensions import AllowedExtensionsModel
from ..usecases.get_allowed_extensions import get_allowed_extensions

from ..adapters.controllers.image import ImageConvertController

image_model = ImageConvertModel(Image)
handle_image_convert = convert_image(image_model)

allowed_extensions_model = AllowedExtensionsModel()
handle_get_allowed_extensions = \
  get_allowed_extensions(allowed_extensions_model)

image_controller = \
  ImageConvertController(handle_image_convert, handle_get_allowed_extensions)