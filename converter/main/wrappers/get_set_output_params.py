from collections.abc import Callable


def get_set_output_params(format_output_params_model) -> Callable:
    def inner(output_format, output_params) -> dict:
        return format_output_params_model.get_set_output_params(
            output_format, output_params
        )

    return inner
