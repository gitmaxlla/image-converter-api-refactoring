from collections.abc import Callable


def get_output_format_params(output_format_model) -> Callable:
    def inner(format) -> dict:
        return output_format_model.get_format_params(format)

    return inner
