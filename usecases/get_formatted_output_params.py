def get_formatted_output_params(format_output_params_model):
    def inner(output_format, output_params):
        return format_output_params_model.get_formatted_output_params(
            output_format, output_params
        )
    
    return inner