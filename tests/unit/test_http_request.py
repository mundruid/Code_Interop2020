import requests_mock
import pytest
import json

from examples import http_request


@pytest.fixture
def sample_json():
    with open("tests/fixtures/sample.json") as f:
        return json.load(f)


class TestRequest:
    def test_get_json(self, sample_json):
        mock_response = sample_json
        with requests_mock.Mocker() as req:
            req.get(
                "https://test_url/json",
                json=mock_response,
                headers={"Content-Type": "application/json"},
            )
            resp = http_request.get_json("https://test_url")

        assert resp.ok
        assert resp.json()["slideshow"]["author"] == "Yours Truly"
