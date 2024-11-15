from PIL import Image

from ..utils.constants import ALLOWED_EXTENSIONS
from ..adapters.models.image import ImageConvertModel
from ..usecases.convert_image import convert_image
from ..adapters.controllers.image import ImageConvertController

image_model = ImageConvertModel(Image, ALLOWED_EXTENSIONS)
handle_image_convert = convert_image(image_model)

image_controller = ImageConvertController(handle_image_convert)