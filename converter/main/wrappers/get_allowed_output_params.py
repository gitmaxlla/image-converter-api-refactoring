from collections.abc import Callable


def get_allowed_output_params(allowed_output_params_model) -> Callable:
    def inner(output_format) -> dict:
        return allowed_output_params_model.get_format_params(output_format)

    return inner
