from ...utils.constants import FORMAT_PARAMS

class OutputParamsModel:
    def __init__(self):
        self.__output_format_params = FORMAT_PARAMS

    def get_format_params(self, format):
        return self.__output_format_params[format]