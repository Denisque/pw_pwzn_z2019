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

# def sort_dates(date_str, date_format=''):
#     """
#     Parses and sorts given message to list of datetimes objects descending.
#
#     :param date_str: log of events in time
#     :type date_str: str
#     :param date_format: event format
#     :type date_format: str
#     :return: sorted desc list of utc datetime objects
#     :rtype: list
#     """


def group_dates(dates):
    """
    Groups list of given days day by day.

    :param dates: List of dates to group.
    :type dates: list
    :return:
    """
    data = dates
    data = list(map(lambda x: x.strftime("%Y-%m-%d"), data))
    data_set = set(data)


def format_day(day, events):
    """
    Formats message for one day.

    :param day: Day object.
    :type day: datettime.datetime
    :param events: List of events of given day
    :type events: list
    :return: parsed message for day
    :rtype: str
    """
    pass


def fun1(_str):
    #tmp = 'Sun 10 May 2015 13:54:36 -0700'
    tmp = _str
    data_time_obj = datetime.datetime.strptime(tmp, '%a %d %b %Y %X %z')
    data_time_obj = data_time_obj.astimezone(pytz.utc)
    return data_time_obj


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
    data = sorted(data, reverse=True)
    print(data)
    data = list(map(lambda x: fun1(x), data))
    print(data)






if __name__ == '__main__':
    dates = """
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000
    """
    parse_dates(dates)


    # assert sort_dates(dates) == [
    #     datetime.datetime(2015, 5, 10, 20, 54, 36, tzinfo=datetime.timezone.utc),
    #     datetime.datetime(2015, 5, 10, 13, 54, 36, tzinfo=datetime.timezone.utc),
    #     datetime.datetime(2015, 5, 2, 14, 24, 36, tzinfo=datetime.timezone.utc),
    #     datetime.datetime(2015, 5, 1, 13, 54, 36, tzinfo=datetime.timezone.utc),
    # ]

    # assert parse_dates(dates) == """2015-05-10
    # \t20:54:36
    # \t13:54:36
    # ----
    # 2015-05-02
    # \t14:24:36
    # ----
    # 2015-05-01
    # \t13:54:36"""