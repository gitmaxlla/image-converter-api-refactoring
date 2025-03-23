from PIL import Image

from ..adapters.controllers.image import ImageConvertController
from ..adapters.models.image import ImageConvertModel
from ..adapters.models.io import \
  AllowedInputFileExtensionsModel, AllowedOutputFormatsModel, \
  AllowedOutputParamsModel, FormatOutputParamsModel

from ..wrappers.convert_image import convert_image

from ..wrappers.get_allowed_input_file_extensions import \
  get_allowed_input_file_extensions

from ..wrappers.get_allowed_output_formats import \
  get_allowed_output_formats

from ..wrappers.get_allowed_output_params import \
  get_allowed_output_params

from ..wrappers.get_set_output_params import \
  get_set_output_params

handle_image_convert = convert_image(ImageConvertModel(Image))

handle_get_allowed_input_file_extensions = \
  get_allowed_input_file_extensions(AllowedInputFileExtensionsModel())

handle_get_allowed_output_formats = \
  get_allowed_output_formats(AllowedOutputFormatsModel())

handle_get_allowed_output_params = \
  get_allowed_output_params(AllowedOutputParamsModel())

handle_get_set_output_params = \
  get_set_output_params(FormatOutputParamsModel())

image_convert_controller = ImageConvertController(
  handle_image_convert,
  handle_get_allowed_input_file_extensions,
  handle_get_allowed_output_formats,
  handle_get_allowed_output_params,
  handle_get_set_output_params
)
