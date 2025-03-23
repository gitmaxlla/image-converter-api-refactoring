def get_output_format_params(output_format_model):
  def inner(format):
    return output_format_model.get_format_params(format)
  
  return inner