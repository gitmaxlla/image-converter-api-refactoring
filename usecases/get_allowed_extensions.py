def get_allowed_extensions(allowed_extensions_model):
    def inner():
        return allowed_extensions_model.get_all()
    
    return inner