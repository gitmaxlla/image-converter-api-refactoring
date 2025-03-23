from ..adapters.models.output import OutputParamsModel
from ..adapters.controllers.output import OutputParamsController
from ..wrappers.get_output_format_params import get_output_format_params

handle_get_output_format_params = \
  get_output_format_params(OutputParamsModel())

output_params_controller = \
  OutputParamsController(handle_get_output_format_params)
