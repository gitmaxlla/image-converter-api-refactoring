from ..adapters.models.extensions import AllowedExtensionsModel
from ..usecases.get_allowed_extensions import get_allowed_extensions
from ..adapters.controllers.extensions import AllowedExtensionsController

allowed_extensions_model = AllowedExtensionsModel()
handle_get_allowed_extensions = \
  get_allowed_extensions(allowed_extensions_model)

allowed_extensions_controller = \
  AllowedExtensionsController(handle_get_allowed_extensions)