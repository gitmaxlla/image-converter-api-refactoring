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
            mod_args = {}
            for arg in kwargs:
                mod_args[arg] = kwargs[arg]

            with self.__processor.open(input_image) as image:
                if mod_args.get("exif") == True:
                    mod_args["exif"] = image.getexif()
                    
                image.save(
                    output_image_path,
                    output_format,
                    **mod_args
                )
        except Exception as err:
            raise Exception(f"Convertion processor error: {err}")
        
        return output_image_path