from PIL import Image

from ..utils.constants import ALLOWED_EXTENSIONS
from ..adapters.models.image import ImageModel
from ..usecases.convert_image import convert_image
from ..adapters.controllers.image import ImageController

image_model = ImageModel(Image, ALLOWED_EXTENSIONS)
handle_image_convert = convert_image(image_model)

image_controller = ImageController(handle_image_convert)