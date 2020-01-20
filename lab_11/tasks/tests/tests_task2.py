import pytest
import requests
import requests_mock
from unittest.mock import patch
from lab_11.tasks.tools.metaweather import (
    get_metaweather,
    get_cities_woeid
)


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def raise_for_status(self):
            return self.status_code

    if args[0] == 0: #'https://www.metaweather.com/api/location/search/?query=(War)':
        return MockResponse([{"title": "Warsaw", "woeid": 523920},
        {"title": "Newark", "woeid": 2459269}], 200)
    elif args[0] == 1: #'https://www.metaweather.com/api/location/search/?query=(Warszawa)':
        return MockResponse({}, 200)

    return MockResponse(None, 404)


def test_get_cities_woeid_out_empty():
    resp_mock = mocked_requests_get(1)
    with patch("requests.get", return_value=resp_mock):
        assert get_cities_woeid('Warszawa') == {}

def test_get_cities_woeid_out_war():
    resp_mock = mocked_requests_get(0)
    with patch("requests.get", return_value=resp_mock):
        assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }

def test_get_cities_woeid_out_timeout():
    resp_mock = requests_mock.Adapter()
    resp_mock = resp_mock.register_uri('GET', 'mock://test.com/6', exc=requests.exceptions.Timeout)
    with patch("requests.get", return_value=resp_mock):
        try:
            get_cities_woeid('Warszawa', 0.1)
        except Exception as exc:
            isinstance(exc, requests.exceptions.Timeout)




# def test_one():
#     with requests_mock.Mocker() as m:
#         m.register_uri(method='GET', url='http://test.com', status_code=200, additional_matcher=raise_for_status)
#         with patch('requests.get', return_value=m):
#             get_cities_woeid('Warszawa')
# test_one()