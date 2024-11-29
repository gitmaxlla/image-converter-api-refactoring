from ..adapters.models.io import AllowedIOModel
from ..usecases.get_allowed_io import get_allowed_io
from ..adapters.controllers.io import AllowedIOController

allowed_IO_model = AllowedIOModel()
handle_get_allowed_io = \
  get_allowed_io(allowed_IO_model)

allowed_IO_controller = \
  AllowedIOController(handle_get_allowed_io)