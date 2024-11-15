def convert_image(image_convert_model):
    def inner(input_image, output_image_path, output_format, **kwargs):
        return image_convert_model.convert(
            input_image,
            output_image_path,
            output_format,
            **kwargs
        )
    
    return inner