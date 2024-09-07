def convert_image(ImageModel):
    def inner(input_image, output_image_path, output_format, **kwargs):
        return ImageModel.convert(
            input_image,
            output_image_path,
            output_format,
            **kwargs
        )
    
    return inner