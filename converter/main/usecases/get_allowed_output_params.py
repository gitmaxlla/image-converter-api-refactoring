def get_allowed_output_params(allowed_output_params_model):
  def inner(output_format):
    return allowed_output_params_model.get_format_params(output_format)
  
  return inner