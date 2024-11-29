def get_allowed_io(allowed_io_model):
    def inner():
        return allowed_io_model.get_io_params()
    
    return inner