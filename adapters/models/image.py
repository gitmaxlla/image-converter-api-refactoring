class ImageConvertModel:
    def __init__(self, image_processor, allowed_extensions):
        self.__processor = image_processor
        self.allowed_extensions = allowed_extensions

    def convert(self, input_image, output_image_path, output_format, **kwargs):
        """
        Converts an image to the specified format.
        Raises an exception if an error ocurrs.
        Returns the image path of the converted output.
        """
        if not isinstance(output_image_path, str):
            raise Exception("Output image path must be a string.")

        try:
            with self.__processor.open(input_image) as image:
                image.save(
                    output_image_path,
                    output_format,
                    **kwargs
                )
        except:
            raise Exception("There was an error processing the image.")
        
        return output_image_path