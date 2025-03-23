from collections.abc import Callable


def get_allowed_output_formats(allowed_output_formats_model) -> Callable:
    def inner() -> dict:
        return allowed_output_formats_model.get_all()

    return inner
