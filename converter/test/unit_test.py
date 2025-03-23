from ..main.app import app
from pathlib import Path
import json
from PIL import Image
from pytest import raises

app.config.update({ "TESTING": True })
client = app.test_client()

test_resources = Path(__file__).parent / 'resources'
default_output_params = {
    "png": {"compress_level": 6},
    "ico": {"sizes": [64, 64]},
    "jpeg": {"quality": 50},
    "webp" : {"lossless": 0}
}

def test_server_available():
    assert successfulResponse(client.get('/'))

class TestInfoRoutes:
    def test_allowed_io_params_route(self):
        response = client.get('/allowed-io-params')
        assert "input" in response.json and \
               "output" in response.json

    def test_output_format_params_ico(self):
        assert output_format_params_is_available("ico")

    def test_output_format_params_png(self):
        assert output_format_params_is_available("png")

    def test_output_format_params_webp(self):
        assert output_format_params_is_available("webp")

    def test_output_format_params_jpeg(self):
        assert output_format_params_is_available("jpeg")

    def test_output_format_params_jpg(self):
        # Only JPEG is valid as an output parameter, not JPG 

        response = client.post('/output-format-params', data={
            "output_format": "jpg"
        })

        assert not successfulResponse(response)

class TestConvertions:
    def test_convert_ico_to_png(self):
        assert convert_from_to_is_successful("ico", "png")

    def test_convert_ico_to_jpeg(self):
        assert convert_from_to_is_successful("ico", "jpeg")

    def test_convert_ico_to_webp(self):
        assert convert_from_to_is_successful("ico", "webp")

    def test_convert_png_to_ico(self):
        assert convert_from_to_is_successful("png", "ico")

    def test_convert_png_to_jpeg(self):
        assert convert_from_to_is_successful("png", "jpeg")

    def test_convert_png_to_webp(self):
        assert convert_from_to_is_successful("png", "webp")

    def test_convert_jpeg_to_ico(self):
        assert convert_from_to_is_successful("jpeg", "ico")

    def test_convert_jpeg_to_png(self):
        assert convert_from_to_is_successful("jpeg", "png")

    def test_convert_jpeg_to_webp(self):
        assert convert_from_to_is_successful("jpeg", "webp")

    def test_png_to_png(self):
        assert convert_from_to_is_successful("png", "png")

    def test_jpeg_to_jpeg(self):
        assert convert_from_to_is_successful("jpeg", "jpeg")
        
    def test_webp_to_webp(self):
        assert convert_from_to_is_successful("webp", "webp")

class TestConvertionErrors:
    def test_corrupted_image(self):
        file_config = json.dumps({
                "outputFormat": "jpeg",
                "outputParams": default_output_params["jpeg"]
        })

        file_name = "sample_corrupt.png"

        response = post_to_convert(file_name, file_config)
        assert "error saving" in response.json["data"]["message"]

    def test_no_parameters(self):
        file_config = json.dumps({})

        file_name = "sample.png"

        with raises(KeyError):
            response = post_to_convert(file_name, file_config)

    def test_wrong_parameters(self):
        file_config = json.dumps({
                "outputFormat": "jpeg",
                "outputParams": ""
        })

        file_name = "sample.webp"

        response = post_to_convert(file_name, file_config)
        assert "invalid" in response.json["data"]["message"]

    def test_nonexistent_file(self):
        file_config = json.dumps({
                "outputFormat": "jpeg",
                "outputParams": ""
        })

        file_name = "123"

        with raises(FileNotFoundError):
            response = post_to_convert(file_name, file_config)

    def test_directory_instead_of_a_file(self):
        file_config = json.dumps({
                "outputFormat": "jpeg",
                "outputParams": ""
        })

        file_name = "./"

        with raises(IsADirectoryError):
            response = post_to_convert(file_name, file_config)

    def test_file_upload_size_exceeded(self):
        file_config = json.dumps({
                "outputFormat": "png",
                "outputParams": default_output_params["png"]
        })

        file_name = "sample_big.png"

        response = post_to_convert(file_name, file_config)
        assert "413" in response.status

    def test_invalid_format(self):
        file_config = json.dumps({
                "outputFormat": "image",
                "outputParams": default_output_params["jpeg"]
        })

        file_name = "sample.png"

        with raises(TypeError):
            response = post_to_convert(file_name, file_config)
            assert "Invalid format" in response

class TestKnownBugs:
    def test_convert_ico_to_a_bigger_size(self):
        """
        (To preserve behaviour)
        .ico should logically convert to a bigger size,
        yet only its metadata gets rewritten
        """

        file_config = json.dumps({
                "outputFormat": "ico",
                "outputParams": {
                    "sizes": [128,128]
                }
        })

        file_name = "sample.ico"

        response = post_to_convert(file_name, file_config) 
        assert successfulResponse(response)

        image_path = response.json["data"]["convertionId"]
        with Image.open(image_path) as im:
            assert (128, 128) not in im.info['sizes']

def imageIsValid(path):
    with Image.open(path) as im:
        try:
            im.verify()
            return True
        except:
            return False

def post_to_convert(file_name, file_config):
    return client.post('/convert', data={
        "file_config": file_config,
        "file": ( test_resources / file_name ).open("rb")
    })

def successfulResponse(reponse):
    return "success" in reponse.json["status"]

def output_format_params_is_available(format):
    response = client.post('/output-format-params', data={
        "output_format": format
    })

    return successfulResponse(response)

def convert_from_to_is_successful(format_from, format_to, file_name='sample'):
        file_config = json.dumps({
                "outputFormat": format_to,
                "outputParams": default_output_params[format_to]
        })

        file_name = f"{file_name}.{format_from}"

        response = post_to_convert(file_name, file_config)

        if not successfulResponse(response):
            return False

        image_path = response.json["data"]["convertionId"]
        return imageIsValid(image_path)