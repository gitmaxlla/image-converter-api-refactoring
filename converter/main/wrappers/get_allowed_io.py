from collections.abc import Callable


def get_allowed_io(allowed_io_model) -> Callable:
    def inner() -> dict:
        return allowed_io_model.get_io_params()

    return inner
