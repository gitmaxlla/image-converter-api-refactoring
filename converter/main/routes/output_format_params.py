from ..adapters.models.output import OutputParamsModel
from ..usecases.get_output_format_params import get_output_format_params
from ..adapters.controllers.output import OutputParamsController

output_params_model = OutputParamsModel()
handle_get_output_format_params = \
  get_output_format_params(output_params_model)

output_params_controller = \
  OutputParamsController(handle_get_output_format_params)