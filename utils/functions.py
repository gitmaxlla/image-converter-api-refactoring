def is_file_extension_allowed(filename, allowed_list):
    if not filename:
        return False
    if len(filename) == 0:
        return False
    
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in allowed_list
