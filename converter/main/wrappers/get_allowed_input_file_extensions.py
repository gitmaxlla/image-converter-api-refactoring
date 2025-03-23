from collections.abc import Callable


def get_allowed_input_file_extensions(allowed_extensions_model) -> Callable:
    def inner() -> dict:
        return allowed_extensions_model.get_all()

    return inner
