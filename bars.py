import json

import requests

from math import sqrt
from settings import API_KEY


def fetch_bars_data():
    api_url = 'https://apidata.mos.ru/v1/datasets/1796/rows'
    query_params = {'api_key': API_KEY}
    try:
        raw_response = requests.get(api_url, params=query_params)
        json_response = raw_response.json()
    except requests.exceptions.RequestException:
        json_response = None
    return json_response


def get_biggest_bar(bars_data):
    big_data = max(
        bars_data,
        key=lambda bars: bars['Cells']['SeatsCount']
    )
    big_data_short = {
        'Name': big_data['Cells']['Name'],
        'Address': big_data['Cells']['Address'],
        'Seats': big_data['Cells']['SeatsCount']
    }
    return big_data_short


def get_smallest_bar(bars_data):
    small_data = min(
        bars_data,
        key=lambda bars: bars['Cells']['SeatsCount']
    )
    small_data_short = {
        'Name': small_data['Cells']['Name'],
        'Address': small_data['Cells']['Address'],
        'Seats': small_data['Cells']['SeatsCount']
    }
    return small_data_short


def get_closest_bar(bars_data, latitude, longitude):
    x_user, y_user = latitude, longitude
    for bar_data in bars_data:
        x_bar = float(bar_data['Cells']['geoData']['coordinates'][0])
        y_bar = float(bar_data['Cells']['geoData']['coordinates'][1])
        distance = sqrt((x_bar - x_user)**2 + (y_bar - y_user)**2)
        bar_data['user_distance'] = distance
    closest_bar_data = min(
        bars_data,
        key=lambda bar: bar.get('user_distance')
    )
    closest_bar_data_short = {
        'Name': closest_bar_data['Cells']['Name'],
        'Address': closest_bar_data['Cells']['Address'],
        'Seats': closest_bar_data['Cells']['SeatsCount']
    }
    return closest_bar_data_short


def print_max_min_seats_info(biggest_bar_info, smallest_bar_info):
    print("""\nThe biggest Moscow bar is "{}".
It has {} seats and located at "{}".""".format(
        biggest_bar_info['Name'],
        biggest_bar_info['Seats'],
        biggest_bar_info['Address']
    ))
    print("""\nThe smallest Moscow bar is "{}".
It has {} seats and located at "{}".""".format(
        smallest_bar_info['Name'],
        smallest_bar_info['Seats'],
        smallest_bar_info['Address']
    ))
    print('''\nNow let's find the closest to you bar. Type your coordinates -
latitude and longitude, like: 55.753215 и 37.622504.''')


def print_closest_bar_info(closest_bar_info):
    print('\nThe closest bar is "{}" with {} seats. Address: "{}".'.format(
        closest_bar_info['Name'],
        closest_bar_info['Seats'],
        closest_bar_info['Address']
    ))


def main():
    fetched_data = fetch_bars_data()
    if fetched_data is not None:
        biggest_bar_info = get_biggest_bar(fetched_data)
        smallest_bar_info = get_smallest_bar(fetched_data)
        print_max_min_seats_info(biggest_bar_info, smallest_bar_info)
        try:
            user_latitude = float(input("\nLatitude:"))
            user_longitude = float(input("Longitude:"))
            closest_bar_info = get_closest_bar(
                fetched_data,
                user_longitude,
                user_latitude
            )
            print_closest_bar_info(closest_bar_info)
        except ValueError as wrong_input_info:
            print(wrong_input_info)
    else:
        print('\nConnection problem - check your internet access.')


if __name__ == '__main__':
    main()
