from ...utils.constants import ALLOWED_IO, FORMAT_PARAMS


class AllowedIOModel:
    def __init__(self):
        self.__allowed_IO = ALLOWED_IO

    def get_io_params(self):
        return self.__allowed_IO


class AllowedInputFileExtensionsModel:
    def __init__(self):
        self.__allowed_extensions = ALLOWED_IO["input"]["file_extensions"]

    def get_all(self):
        return self.__allowed_extensions


class AllowedOutputFormatsModel:
    def __init__(self):
        self.__allowed_output_formats = ALLOWED_IO["output"]["file_formats"]

    def get_all(self):
        return self.__allowed_output_formats


class AllowedOutputParamsModel:
    def __init__(self):
        self.__format_items = FORMAT_PARAMS

    def get_format_params(self, output_format):
        allowed_parameters = self.__format_items[output_format]
        return [parameter["name"] for parameter in allowed_parameters]


class FormatOutputParamsModel:
    def __init__(self):
        self.__format_items = FORMAT_PARAMS

    def __is_bool(self, parameter):
        return parameter.get("is_bool")

    def __is_called(self, parameter, name):
        return parameter.get("name") == name

    def get_set_output_params(self, output_format, output_params):
        params_by_format = self.__format_items[output_format]
        formatted_output_params = dict()

        for paramName in output_params:
            paramValue = output_params[paramName]

            for parameter in params_by_format:
                if self.__is_called(parameter, paramName):
                    if self.__is_bool(parameter) and paramValue == 1:
                        formatted_output_params[paramName] = bool(paramValue)
                elif isinstance(parameter.get("options"), list):
                    formatted_output_params[paramName] = [tuple(paramValue)]
                else:
                    formatted_output_params[paramName] = paramValue

        return formatted_output_params
