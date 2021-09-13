import cv2
from weather_maker import WeatherMaker
import os
import requests

response = requests.get('https://pogoda.mail.ru/prognoz/moskva/24hours/')

IMAGE = "python_snippets/external_data/probe.jpg"

CLOUD = 'python_snippets/external_data/weather_img/cloud.jpg'
RAIN = 'python_snippets/external_data/weather_img/rain.jpg'
SNOW = 'python_snippets/external_data/weather_img/snow.jpg'
SUN = 'python_snippets/external_data/weather_img/sun.jpg'

FILES_IMAGE = 'weather_image'


class ImageMaker:

    def __init__(self, weather_list):
        self.weather_list = weather_list
        self.cloudy = ['дымка', 'облачность', 'малооблачно', 'туман', 'сильный туман', 'облачно',
                       'облачно без существенных осадков']
        self.sunny = ['ясно']
        self.rain = ['пасмурно', 'слабый дождь', 'ливневая крупа', 'ливневый дождь', 'дождь']
        self.snow = ['ливневый снег', 'снег', 'слабый снег']
        self.image = cv2.imread(IMAGE)
        self.width = int(self.image.shape[1])
        self.height = int(self.image.shape[0])
        self.cloud_image = cv2.imread(CLOUD)
        self.rain_image = cv2.imread(RAIN)
        self.snow_image = cv2.imread(SNOW)
        self.sun_image = cv2.imread(SUN)
        self.date = None

    def get_image(self):
        for weather_data in self.weather_list:
            self.date = weather_data['date'].strftime('%d_%m_%Y')
            self.draw_image(weather_data)

    def draw_current_weather(self, current_weather):
        new_image = cv2.putText(
            img=self.image,
            text=current_weather,
            org=(10, 245),
            fontFace=3,
            fontScale=0.9,
            color=(0, 0, 0)
        )
        cv2.imwrite(os.path.join(FILES_IMAGE, f'weather_{self.date}.jpg'), new_image)

    def draw_text(self, text, indent):
        new_image = cv2.putText(
            img=self.image,
            text=text,
            org=(265, 20 + indent),
            fontFace=3,
            fontScale=0.6,
            color=(255, 255, 255)
        )
        cv2.imwrite(os.path.join(FILES_IMAGE, f'weather_{self.date}.jpg'), new_image)

    def draw_text_date(self, text):
        new_image = cv2.putText(
            img=self.image,
            text=text,
            org=(10, 40),
            fontFace=3,
            fontScale=0.9,
            color=(0, 0, 0)
        )
        cv2.imwrite(os.path.join(FILES_IMAGE, f'weather_{self.date}.jpg'), new_image)

    def draw_cloudy(self, image_draw):
        x = 255  # TODO сделайте константы для применяемых кортежей координат и тут присваивайте распаковкой в одну строку
        y = 255
        z = 255
        for width_pixel in range(self.width):  # TODO стоит придумать одну универсальную функцию для рисования
            if width_pixel in range(150):
                cv2.line(self.image, (width_pixel, 0), (width_pixel, self.height), (x, y, z), 1)
            elif width_pixel >= 150:
                if x > 100:
                    x -= 1
                if y > 100:
                    y -= 1
                if z > 100:
                    z -= 1
                cv2.line(self.image, (width_pixel, 0), (width_pixel, self.height), (x, y, z), 1)
        self.image[60: 160, 20: 120] = image_draw

    def draw_rain(self, image_draw):
        x = 255
        y = 255
        z = 255
        for width_pixel in range(self.width):
            if width_pixel in range(150):
                cv2.line(self.image, (width_pixel, 0), (width_pixel, self.height), (x, y, z), 1)
            elif width_pixel >= 150:
                if x > 230:
                    x -= 1
                if y > 0:
                    y -= 2
                if z > 0:
                    z -= 2
                cv2.line(self.image, (width_pixel, 0), (width_pixel, self.height), (x, y, z), 1)
        self.image[60: 160, 20: 120] = image_draw

    def draw_snow(self, image_draw):
        x = 246
        y = 246
        z = 246
        for width_pixel in range(self.width):
            if width_pixel in range(150):
                cv2.line(self.image, (width_pixel, 0), (width_pixel, self.height), (x, y, z), 1)
            elif width_pixel >= 150:
                if y > 200:
                    y -= 1
                if z > 125:
                    z -= 2
                cv2.line(self.image, (width_pixel, 0), (width_pixel, self.height), (x, y, z), 1)
        self.image[60: 160, 20: 120] = image_draw

    def draw_sun(self, image_draw):
        x = 255
        y = 255
        z = 255
        for width_pixel in range(self.width):
            if width_pixel in range(150):
                cv2.line(self.image, (width_pixel, 0), (width_pixel, self.height), (x, y, z), 1)
            elif width_pixel >= 150:
                if x > 15:
                    x -= 2
                if y > 220:
                    y -= 1
                cv2.line(self.image, (width_pixel, 0), (width_pixel, self.height), (x, y, z), 1)
        self.image[60: 160, 20: 120] = image_draw

    def draw_degree(self, degree_number, indent):
        if degree_number == '0':
            # TODO эти две строки кода ниже дублируются за исключением окончания, вот его тут и определяйте, а обе
            #  строки вынесите из условного оператора
            degrees_text = f'{degree_number} градусов Цельсия'
            self.draw_text(degrees_text, indent)
        elif int(degree_number[1:]) in range(10, 21):
            degrees_text = f'{degree_number} градусов Цельсия'
            self.draw_text(degrees_text, indent)
        elif int(degree_number[-1]) == 1:
            degrees_text = f'{degree_number} градус Цельсия'
            self.draw_text(degrees_text, indent)
        elif int(degree_number[-1]) in range(2, 5):
            degrees_text = f'{degree_number} градуса Цельсия'
            self.draw_text(degrees_text, indent)
        else:
            degrees_text = f'{degree_number} градусов Цельсия'
            self.draw_text(degrees_text, indent)

    def draw_image(self, weather_data):
        # TODO попробуйте сделать такую структуру для того чтобы не дублировать код:
        # weather_funcs = {
        #     self.cloudy: (self.draw_cloudy, self.cloud_image),
        #     self.rain: (self.draw_rain, self.rain_image),
        #     ...
        # }
        # напросок варианта использования
        # for wf in weather_funcs:
        #     weather_name = set(wf) & set(weather_data['weather_for_the_day'])
        #     if set(wf) & set(weather_data['weather_for_the_day']):
        #         func, img = weather_funcs[wf]
        #         func(img)
        #         self.draw_current_weather(list(weather_name)[0])

        lack_of_text = True
        if lack_of_text:
            for weather_name in self.cloudy:
                if weather_name in weather_data['weather_for_the_day']:
                    self.draw_cloudy(self.cloud_image)
                    self.draw_current_weather(weather_name)
                    lack_of_text = False
        if lack_of_text:
            for weather_name in self.rain:
                if weather_name in weather_data['weather_for_the_day']:
                    self.draw_rain(self.rain_image)
                    self.draw_current_weather(weather_name)
                    lack_of_text = False
        if lack_of_text:
            for weather_name in self.snow:
                if weather_name in weather_data['weather_for_the_day']:
                    self.draw_snow(self.snow_image)
                    self.draw_current_weather(weather_name)
                    lack_of_text = False
        if lack_of_text:
            for weather_name in self.sunny:
                if weather_name in weather_data['weather_for_the_day']:
                    self.draw_sun(self.sun_image)
                    self.draw_current_weather(weather_name)
                    lack_of_text = False
        if lack_of_text:
            raise ValueError(' Нету такого')

        os.makedirs(FILES_IMAGE, exist_ok=True)

        self.draw_text('Температура:', 0)
        self.draw_text('днем', 50)
        self.draw_degree(weather_data['daytime_temperature'], 80)
        self.draw_text('ночью', 130)
        self.draw_degree(weather_data['night_temperature'], 160)
        self.draw_text_date(weather_data['date'].strftime('%d.%m.%Y'))


weathermaker = WeatherMaker()
imagemaker = ImageMaker(weathermaker.get_forecast())
imagemaker.get_image()

