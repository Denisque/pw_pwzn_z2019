import requests
from urllib.parse import urljoin


def get_cities_woeid(query: str, timeout: float = 5.):
    API_URL = 'https://www.metaweather.com/api/'
    location_url = urljoin(API_URL, 'location/search')

    try:
        response = requests.get(location_url, params=dict(query=query), timeout=timeout)
    except RuntimeError:
        RuntimeError

    try:
        response = requests.get(location_url, params=dict(query=query), timeout=timeout)
    except requests.exceptions.Timeout:
        requests.exceptions.Timeout

    try:
        response.status_code != 200
    except requests.exceptions.HTTPError:
        print(requests.exceptions.HTTPError)

    out = response.json()
    if out == []:
        return {}
    else:
        weid = {}
        for i in range(len(out)):
            tmp = out[i]
            city = tmp['title']
            id = tmp['woeid']
            weid[city] = id
        return weid


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
       'Warsaw': 523920,
       'Newark': 2459269,
    }
    try:
       get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
       isinstance(exc, requests.exceptions.Timeout)
