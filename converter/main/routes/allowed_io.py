from ..adapters.models.io import AllowedIOModel
from ..adapters.controllers.io import AllowedIOController
from ..wrappers.get_allowed_io import get_allowed_io

handle_get_allowed_io = \
  get_allowed_io(AllowedIOModel())

allowed_IO_controller = \
  AllowedIOController(handle_get_allowed_io)
