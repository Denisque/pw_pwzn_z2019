"""
Zadanie za 2 pkt.

Uzupełnij funckję parse_dates tak by zwracała przygotowaną wiadomość
z posortowanymi zdarzeniami.
Funkcja przyjmuje ciag zdarzeń (zapisanych w formie timestampu w dowolnej strefie czasowej),
przetwarza je na zdarzenia w strefie czasowej UTC i sortuje.
Posortowane zdarzenia są grupowane na dni i wypisywane od najnowszych do najstarszych.

Na 1pkt. Uzupełnij funkcję sort_dates, która przyjmuje dwa parametry:
- log (wielolinijkowy ciąg znaków z datami) zdarzeń
- format daty (podany w assercie format ma być domyślnym)
Zwraca listę posortowanych obiektów typu datetime w strefie czasowej UTC.

Funkcje group_dates oraz format_day mają pomoc w grupowaniu kodu.
UWAGA: Proszę ograniczyć użycie pętli do minimum.
"""

import datetime
import pytz

def sort_dates(date_str, date_format=''):
    """
    Parses and sorts given message to list of datetimes objects descending.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: sorted desc list of utc datetime objects
    :rtype: list
    """
    data = date_str.strip()
    data = data.splitlines()
    data = list(map(lambda x: x.strip(), data))
    data_list = list(map(lambda x: str2dt(x), data))
    data_list = sorted(data_list, reverse=True)
    return data_list



def str2dt(_str):
    """
    Changing string date to list datetime format.

    :param _str: date as string
    :type date_str: str
    :return: datatime object in UTC
    :rtype: datatime
    """

    date_time = datetime.datetime.strptime(_str, "%a %d %b %Y %X %z")
    date_time = date_time.astimezone(pytz.utc)
    return date_time


def parse_dates(date_str, date_format=''):
    """
    Parses and groups (in UTC) given list of events.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: parsed events
    :rtype: str
    """

    data = date_str.strip()
    data = data.splitlines()
    data = list(map(lambda x: x.strip(), data))
    data_list = list(map(lambda x: str2dt(x), data))
    data_list = sorted(data_list, reverse=True)

    current_day = data_list[0].strftime("%Y-%m-%d")
    output = current_day
    for day in range(len(data_list)):
        if data_list[day].strftime("%Y-%m-%d") != current_day:
            output += '\n    ----'
            current_day = data_list[day].strftime("%Y-%m-%d")
            output += '\n    '
            output += current_day
        output += '\n    '
        output += data_list[day].strftime("\t%X")
    return output


if __name__ == '__main__':
    dates = """
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000
    """

    assert sort_dates(dates) == [
        datetime.datetime(2015, 5, 10, 20, 54, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 10, 13, 54, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 2, 14, 24, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 1, 13, 54, 36, tzinfo=datetime.timezone.utc),
    ]

assert parse_dates(dates) == """2015-05-10
    \t20:54:36
    \t13:54:36
    ----
    2015-05-02
    \t14:24:36
    ----
    2015-05-01
    \t13:54:36"""
