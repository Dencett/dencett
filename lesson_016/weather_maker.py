import requests
import lxml.html
import re
import datetime

# URL = 'https://pogoda.mail.ru/prognoz/moskva/'

re_degree = re.compile(r'[-+]?[\d]+')
re_weather = re.compile(r'[а-я]+')
weather_by_day = {
    0: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/a/div[1]/div[1]/text()',
        'night_temperature': '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/a/div[2]/div[3]/text()',
        'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/a/div[2]/div/text()',
        'date': datetime.datetime.now()},
    1: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/a/div[3]/text()',
        'night_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/a/div[3]/span/text()',
        'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/a/div[4]/text()',
        'date': (datetime.datetime.now() + datetime.timedelta(days=1))},
    2: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/a/div[3]/text()',
        'night_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/a/div[3]/span/text()',
        'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/a/div[4]/text()',
        'date': (datetime.datetime.now() + datetime.timedelta(days=2))},
    3: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[3]/a/div[3]/text()',
        'night_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[3]/a/div[3]/span/text()',
        'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[3]/a/div[4]/text()',
        'date': (datetime.datetime.now() + datetime.timedelta(days=3))},
    4: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[4]/a/div[3]/text()',
        'night_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[4]/a/div[3]/span/text()',
        'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[4]/a/div[4]/text()',
        'date': (datetime.datetime.now() + datetime.timedelta(days=4))},
    5: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[5]/a/div[3]/text()',
        'night_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[5]/a/div[3]/span/text()',
        'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[5]/a/div[4]/text()',
        'date': (datetime.datetime.now() + datetime.timedelta(days=5))},
    6: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[6]/a/div[3]/text()',
        'night_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[6]/a/div[3]/span/text()',
        'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[6]/a/div[4]/text()',
        'date': (datetime.datetime.now() + datetime.timedelta(days=6))},
    7: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/a/div[3]/text()',
        'night_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/a/div[3]/span/text()',
        'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[7]/a/div[4]/text()',
        'date': (datetime.datetime.now() + datetime.timedelta(days=7))},
    8: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[8]/a/div[3]/text()',
        'night_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[8]/a/div[3]/span/text()',
        'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[8]/a/div[4]/text()',
        'date': (datetime.datetime.now() + datetime.timedelta(days=8))},
    9: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[9]/a/div[3]/text()',
        'night_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[9]/a/div[3]/span/text()',
        'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[9]/a/div[4]/text()',
        'date': (datetime.datetime.now() + datetime.timedelta(days=9))},
    10: {'daytime_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[10]/a/div[3]/text()',
         'night_temperature': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[10]/a/div[3]/span/text()',
         'weather_for_the_day': '/html/body/div[1]/div[2]/div/div[3]/div[1]/div/div/div/div[10]/a/div[4]/text()',
         'date': (datetime.datetime.now() + datetime.timedelta(days=10))}
}


class WeatherMaker:

    def __init__(self):
        self.url = 'https://pogoda.mail.ru/prognoz/moskva/'  # TODO вынесите урл в константу
        self.weather_list = []
        self.weather_by_day = weather_by_day

    def get_forecast(self):
        response = requests.get(self.url)
        html_tree = lxml.html.document_fromstring(response.text)
        while True:
            days = input('Выберите количество дней для прогноза (минимум 0 (только на сегодня), максимум 10 дней): ')
            if int(days) in range(0, 11):
                break
        for day in range(0, int(days) + 1):
            html_daytime_temperature = html_tree.xpath(self.weather_by_day[day]['daytime_temperature'])
            html_night_temperature = html_tree.xpath(self.weather_by_day[day]['night_temperature'])
            html_weather_for_the_day = html_tree.xpath(self.weather_by_day[day]['weather_for_the_day'])
            daytime_temperature = re.findall(re_degree, ''.join(html_daytime_temperature))
            night_temperature = re.findall(re_degree, ''.join(html_night_temperature))
            weather_for_the_day = re.findall(re_weather, ''.join(html_weather_for_the_day))
            self.weather_list.append(
                {'daytime_temperature': daytime_temperature[0],
                 'night_temperature': night_temperature[0],
                 'weather_for_the_day': ' '.join(weather_for_the_day),
                 'date': self.weather_by_day[day]['date']}
            )
        return self.weather_list


# weather_maker = WeatherMaker()
# print(weather_maker.get_forecast())
# .strftime('%d.%m.%Y')
