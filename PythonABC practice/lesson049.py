# coding=gbk

import json
import datetime
import requests
import time

# Your API key is cec3dff6f05531c688b6818c2cbf8124

App_Key = 'cec3dff6f05531c688b6818c2cbf8124'
#
# tryone  = datetime.datetime.fromtimestamp(time.time())
#
# print(tryone.year)

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M %p')
    return converted_time

def url_builder_name(city_name):

    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    api = 'http://api.openweathermap.org/data/2.5/weather?q='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

    full_api_url = api + city_name + '&lang=zh_cn' + '&units=' + unit + '&APPID=' + App_Key
    return full_api_url

# trythree=respsonse = requests.get(url_builder_name('beijing'))
# print(trythree)


def data_fetch(full_api_url):
    respsonse = requests.get(full_api_url)
    try:
        respsonse.raise_for_status()
    except Exception as exc:
        print('There was a problem:{}'.format(exc))

    return json.loads(respsonse.text)

# tryfour=url_builder_name('beijing')
#
# print(date_fetch(tryfour))
# {'coord': {'lon': 116.4, 'lat': 39.91},
#  'weather': [{'id': 800, 'main': 'Clear', 'description': '晴', 'icon': '01d'
#               }],
#  'base': 'stations',
#  'main': {'temp': 7.78, 'feels_like': 3.04, 'temp_min': 6.67, 'temp_max': 9.44, 'pressure': 1029, 'humidity': 19
#           },
#  'visibility': 10000,
#  'wind': {'speed': 2, 'deg': 110
#           # },
#  'clouds': {'all': 0
#             },
#  'dt': 1583312135,
#  'sys': {'type': 1, 'id': 9609, 'country': 'CN', 'sunrise': 1583275403, 'sunset': 1583316550
#          },
#  'timezone': 28800, 'id': 1816670, 'name': 'Beijing', 'cod': 200
#  }

def data_organzier(raw_data):

    main = raw_data.get('main')
    sys = raw_data.get('sys')
    data = {
        'city':raw_data['name'],
        'country':sys.get('country'),#get() 方法和 [key] 方法的主要区别在于，[key] 在遇到不存在的 key 时会抛出 KeyError 错误。get() 方法和 [key] 方法的主要区别在于，[key] 在遇到不存在的 key 时会抛出 KeyError 错误
        'temp':main.get('temp'),
        'temp_max':main['temp_max'],
        'temp_min':main.get('temp_min'),
        'humidity':main.get('humidity'),
        'pressure':main.get('pressure'),
        'sky':raw_data['weather'][0]['main'],
        'sunrise':time_converter(sys.get('sunrise')),
        'sunset':time_converter(sys.get('sunset')),
        'wind':raw_data.get('wind').get('speed'),
        'wind_deg': raw_data.get('deg'),
        'dt': time_converter(raw_data.get('dt')),
        'cloudiness': raw_data.get('clouds').get('all'),
        'description': raw_data['weather'][0].get('description')
    }
    return data

def data_output(data):

    data['m_symbol'] = '\u00b0' + 'C'

    s = '''
----------------------------------------------
    Current weather in: {city}, {country}:
    {temp}{m_symbol} {sky}
    Max: {temp_max}, Min: {temp_min}

    Wind Speed: {wind}, Degree: {wind_deg}
    Humidity: {humidity}
    Cloud: {cloudiness}
    Pressure: {pressure}
    Sunrise at: {sunrise}
    Sunset at: {sunset}
    Description: {description}

    Last update from the server: {dt}
----------------------------------------------'''
    print(s.format(**data))


city = input('Which city you want to check? ')

url = url_builder_name(city)
rawData = data_fetch(url)
prettyData = data_organzier(rawData)
data_output(prettyData)