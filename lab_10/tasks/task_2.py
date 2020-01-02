import pathlib
import requests
import calendar
import csv

from typing import Optional, Union, List
from urllib.parse import urljoin


API_URL = 'https://www.metaweather.com/api/'


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):

    # 1. Jezeli brak sciezki
    if path == None:
        if month in range(10):
            path = pathlib.Path.cwd() / f'{woeid}_{year}_0{month}'
        else:
            path = pathlib.Path.cwd() / f'{woeid}_{year}_{month}'
        path.mkdir(parents=True, exist_ok=True)
        monthRange = calendar.monthrange(year, month)
        name_saved_files = []
        for day in range(1, monthRange[1]+1):
            location_url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')
            try:
                response = requests.get(location_url, timeout=timeout)
            except RuntimeError:
                RuntimeError
            try:
                response = requests.get(location_url, timeout=timeout)
            except requests.exceptions.Timeout:
                requests.exceptions.Timeout
            try:
                response.status_code != 200
            except requests.exceptions.HTTPError:
                print(requests.exceptions.HTTPError)
            response = requests.get(location_url, timeout=timeout)
            data = response.json()
            file_name = f'{year}_{month}_{day}.csv'
            with open(path / file_name, 'w') as _file:
                writer = csv.DictWriter(_file, delimiter=',', quotechar='"', fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            name_saved_files.append(file_name)
        return str(path), name_saved_files

    # 2. Podana jest ścieżka bezwzględna - nie edytuj ścieżki zapisu,
    elif path[0] is '/':
        path.mkdir(parents=True, exist_ok=True)
        monthRange = calendar.monthrange(year, month)
        name_saved_files = []
        for day in range(1, monthRange[1] + 1):
            print(day)
            location_url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')
            try:
                response = requests.get(location_url, timeout=timeout)
            except RuntimeError:
                RuntimeError
            try:
                response = requests.get(location_url, timeout=timeout)
            except requests.exceptions.Timeout:
                requests.exceptions.Timeout
            try:
                response.status_code != 200
            except requests.exceptions.HTTPError:
                print(requests.exceptions.HTTPError)
            response = requests.get(location_url, timeout=timeout)
            data = response.json()
            file_name = f'{year}_{month}_{day}.csv'
            with open(path / file_name, 'w') as _file:
                writer = csv.DictWriter(_file, delimiter=',', quotechar='"', fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            name_saved_files.append(file_name)
        return str(path), name_saved_files

    # 3.podana jest ścieżka względna - miejscem zapisu jest podana ścieżka w folderze uruchomienia pliku
    else:
        if month in range(10):
            path_out = path + '/' + f'{woeid}_{year}_0{month}'
            path = pathlib.Path.cwd() / path / f'{woeid}_{year}_0{month}'
        else:
            path_out = path + '/' + f'{woeid}_{year}_{month}'
            path = pathlib.Path.cwd() / path / f'{woeid}_{year}_{month}'
        path.mkdir(parents=True, exist_ok=True)
        monthRange = calendar.monthrange(year, month)
        name_saved_files = []
        for day in range(1, monthRange[1]+1):
            location_url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')
            try:
                response = requests.get(location_url, timeout=timeout)
            except RuntimeError:
                RuntimeError
            try:
                response = requests.get(location_url, timeout=timeout)
            except requests.exceptions.Timeout:
                requests.exceptions.Timeout
            try:
                response.status_code != 200
            except requests.exceptions.HTTPError:
                print(requests.exceptions.HTTPError)
            response = requests.get(location_url, timeout=timeout)
            data = response.json()
            if data == []:
                pass
            else:
                file_name = f'{year}_{month}_{day}.csv'
                with open(path / file_name, 'w') as _file:
                    writer = csv.DictWriter(_file, delimiter=',', quotechar='"', fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
                name_saved_files.append(file_name)
        return path_out, name_saved_files



if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
