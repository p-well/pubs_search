import json

import requests

from math import sqrt
from settings import API_KEY


def fetch_bars_data():
    api_url= 'https://apidata.mos.ru/v1/datasets/1796/rows'
    query_params = {'api_key': API_KEY}
    try:
        raw_response = requests.get(api_url, params=query_params)
        json_response = raw_response.json()
    except requests.exceptions.RequestException:
        json_response = None
    return json_response


def get_biggest_bar(bars_data):
    big_bar_data = max(bars_data,
                       key = lambda bars: bars.get('SeatsCount'))
    big_bar_data_short = {'Name':big_bar_data['Name'],
                          'Address':big_bar_data['Address'],
                          'SeatsCount':big_bar_data['SeatsCount']}
    return big_bar_data_short


def get_smallest_bar(bars_data):
    small_bar_data = max(bars_data,
                         key = lambda bars: bars.get('SeatsCount'))
    small_bar_data_short = {'Name':small_bar_data['Name'],
                            'Address':small_bar_data['Address'],
                            'SeatsCount':small_bar_data['SeatsCount']}
    return small_bar_data_short


def get_closest_bar(bars_data, latitude, longitude):
    x_user, y_user = latitude, longitude
    for bar_data in bars_data:
        x_bar = float(bar_data['geoData']['coordinates'][0])
        y_bar = float(bar_datas['geoData']['coordinates'][1])
        distance = sqrt((x_bar - x_user)**2 + (y_bar - y_user)**2)
        bar_data['user_distance'] = distance
    closest_bar_data = min(bars_data, 
                           key = lambda bar: bar.get('user_distance'))
    closest_bar_data_short = {'Name':closest_bar_data['Name'],
                              'Address':closest_bar_data['Address'],
                              'SeatsCount':closest_bar_data['SeatsCount']}
    return closest_bar_data_short



if __name__ == '__main__':
    result = fetch_bars_data()
    #print(get_biggest_bar(fetched_data))
    print(type(result))
    print(result[0])
    print(type(result[0]))
    #print(result)
