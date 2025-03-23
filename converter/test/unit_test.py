from ..main.app import create_app
from pathlib import Path
import pytest
import json
from PIL import Image


@pytest.fixture()
def app():
    app = create_app("./converter/test/uploads")
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


test_resources = Path(__file__).parent / 'resources'
default_output_params = {
    "png": {"compress_level": 6},
    "ico": {"sizes": [64, 64]},
    "jpeg": {"quality": 50},
    "webp": {"lossless": 0}
}


def test_server_available(client):
    assert successfulResponse(client.get('/'))


class TestInfoRoutes:
    def test_allowed_io_params_route(self, client):
        response = client.get('/allowed-io-params')
        assert "input" in response.json and \
               "output" in response.json

    def test_output_format_params_ico(self, client):
        assert output_format_params_is_available("ico", client)

    def test_output_format_params_png(self, client):
        assert output_format_params_is_available("png", client)

    def test_output_format_params_webp(self, client):
        assert output_format_params_is_available("webp", client)

    def test_output_format_params_jpeg(self, client):
        assert output_format_params_is_available("jpeg", client)

    def test_output_format_params_jpg(self, client):
        # Only JPEG is valid as an output parameter, not JPG

        response = client.post('/output-format-params', data={
            "output_format": "jpg"
        })

        assert not successfulResponse(response)


class TestConvertions:
    def test_convert_ico_to_png(self, client):
        assert convert_from_to_is_successful("ico", "png", "sample", client)

    def test_convert_ico_to_jpeg(self, client):
        assert convert_from_to_is_successful("ico", "jpeg", "sample", client)

    def test_convert_ico_to_webp(self, client):
        assert convert_from_to_is_successful("ico", "webp", "sample", client)

    def test_convert_png_to_ico(self, client):
        assert convert_from_to_is_successful("png", "ico", "sample", client)

    def test_convert_png_to_jpeg(self, client):
        assert convert_from_to_is_successful("png", "jpeg", "sample", client)

    def test_convert_png_to_webp(self, client):
        assert convert_from_to_is_successful("png", "webp", "sample", client)

    def test_convert_jpeg_to_ico(self, client):
        assert convert_from_to_is_successful("jpeg", "ico", "sample", client)

    def test_convert_jpeg_to_png(self, client):
        assert convert_from_to_is_successful("jpeg", "png", "sample", client)

    def test_convert_jpeg_to_webp(self, client):
        assert convert_from_to_is_successful("jpeg", "webp", "sample", client)

    def test_png_to_png(self, client):
        assert convert_from_to_is_successful("png", "png", "sample", client)

    def test_jpeg_to_jpeg(self, client):
        assert convert_from_to_is_successful("jpeg", "jpeg", "sample", client)

    def test_webp_to_webp(self, client):
        assert convert_from_to_is_successful("webp", "webp", "sample", client)


class TestConvertionErrors:
    def test_corrupted_image(self, client):
        file_config = json.dumps({
                "outputFormat": "jpeg",
                "outputParams": default_output_params["jpeg"]
        })

        file_name = "sample_corrupt.png"

        response = post_to_convert(file_name, file_config, client)
        assert "error saving" in response.json["data"]["message"]

    def test_no_parameters(self, client):
        file_config = json.dumps({})

        file_name = "sample.png"

        with pytest.raises(KeyError):
            post_to_convert(file_name, file_config, client)

    def test_wrong_parameters(self, client):
        file_config = json.dumps({
                "outputFormat": "jpeg",
                "outputParams": ""
        })

        file_name = "sample.webp"

        response = post_to_convert(file_name, file_config, client)
        assert "invalid" in response.json["data"]["message"]

    def test_nonexistent_file(self, client):
        file_config = json.dumps({
                "outputFormat": "jpeg",
                "outputParams": ""
        })

        file_name = "123"

        with pytest.raises(FileNotFoundError):
            post_to_convert(file_name, file_config, client)

    def test_directory_instead_of_a_file(self, client):
        file_config = json.dumps({
                "outputFormat": "jpeg",
                "outputParams": ""
        })

        file_name = "./"

        with pytest.raises(IsADirectoryError):
            post_to_convert(file_name, file_config, client)

    def test_file_upload_size_exceeded(self, client):
        file_config = json.dumps({
                "outputFormat": "png",
                "outputParams": default_output_params["png"]
        })

        file_name = "sample_big.png"

        response = post_to_convert(file_name, file_config, client)
        assert "413" in response.status

    def test_invalid_format(self, client):
        file_config = json.dumps({
                "outputFormat": "image",
                "outputParams": default_output_params["jpeg"]
        })

        file_name = "sample.png"

        with pytest.raises(TypeError):
            response = post_to_convert(file_name, file_config, client)
            assert "Invalid format" in response


class TestKnownBugs:
    def test_convert_ico_to_a_bigger_size(self, client):
        """
        (To preserve behaviour)
        .ico should logically convert to a bigger size,
        yet only its metadata gets rewritten
        """

        file_config = json.dumps({
                "outputFormat": "ico",
                "outputParams": {
                    "sizes": [128, 128]
                }
        })

        file_name = "sample.ico"

        response = post_to_convert(file_name, file_config, client)
        assert successfulResponse(response)

        image_path = response.json["data"]["convertionId"]
        with Image.open(image_path) as im:
            assert (128, 128) not in im.info['sizes']


def imageIsValid(path):
    with Image.open(path) as im:
        try:
            im.verify()
            return True
        except Exception:
            return False


def post_to_convert(file_name, file_config, client):
    return client.post('/convert', data={
        "file_config": file_config,
        "file": (test_resources / file_name).open("rb")
    })


def successfulResponse(reponse):
    return "success" in reponse.json["status"]


def output_format_params_is_available(format, client):
    response = client.post('/output-format-params', data={
        "output_format": format
    })

    return successfulResponse(response)


def convert_from_to_is_successful(format_from, format_to, file_name, client):
    file_config = json.dumps({
            "outputFormat": format_to,
            "outputParams": default_output_params[format_to]
    })

    file_name = f"{file_name}.{format_from}"

    response = post_to_convert(file_name, file_config, client)

    if not successfulResponse(response):
        return False

    image_path = response.json["data"]["convertionId"]
    return imageIsValid(image_path)
