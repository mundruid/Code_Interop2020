import unittest
import mock

from examples import arista


class TestArista:
    @mock.patch("examples.arista.connect_to_arista", autospec=True)
    def test_connect_to_arista_eos_success(self, mock_miko):
        fixture = {
            "device_type": "lalala",
            "host": "test_host",
            "username": "test_user",
            "password": "test_password",
        }
        result = arista.connect_to_arista(
            device_type="lalala",
            host="test_host",
            username="test_user",
            password="test_password",
        )

        mock_miko.assert_called_with(**fixture)
        assert result != None
