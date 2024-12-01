def get_allowed_output_formats(allowed_output_formats_model):
  def inner():
    return allowed_output_formats_model.get_all()
  
  return inner