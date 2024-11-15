class ImageConvertModel:
    def __init__(self, image_processor):
        self.__processor = image_processor

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
        except Exception as err:
            raise Exception(f"Convertion processor error: {err}")
        
        return output_image_path