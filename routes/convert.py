from PIL import Image

from ..adapters.models.image import ImageConvertModel
from ..usecases.convert_image import convert_image
from ..adapters.controllers.image import ImageConvertController

image_model = ImageConvertModel(Image)
handle_image_convert = convert_image(image_model)

image_controller = ImageConvertController(handle_image_convert)