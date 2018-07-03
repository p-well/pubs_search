import json

import requests

from settings import API_KEY


def fetch_bars_data():
    api_url= 'https://apidata.mos.ru/v1/datasets/1796/rows'
    query_params = {'api_key': API_KEY}
    try:
        raw_response = requests.get(api_url, params=query_params)
        result = raw_response.json()
    except requests.exceptions.RequestException:
        result = None
    return result


#def get_biggest_bar():#


#def get_smallest_bar():


#def get_closed_bar():


if __name__ == '__main__':
    result = fetch_bars_data()
    print(type(result))
    print(result[0])
    #print(result)
