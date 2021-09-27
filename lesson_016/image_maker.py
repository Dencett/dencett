import cv2
from weather_maker import WeatherMaker
from database_updater import DatabaseUpdater
import os
import requests

response = requests.get('https://pogoda.mail.ru/prognoz/moskva/24hours/')

IMAGE = "python_snippets/external_data/probe.jpg"

CLOUD = 'python_snippets/external_data/weather_img/cloud.jpg'
RAIN = 'python_snippets/external_data/weather_img/rain.jpg'
SNOW = 'python_snippets/external_data/weather_img/snow.jpg'
SUN = 'python_snippets/external_data/weather_img/sun.jpg'

FILES_IMAGE = 'weather_image'

BGR_B = 255
BGR_G = 255
BGR_R = 255


class ImageMaker:

    def __init__(self, weather_list):
        self.weather_list = weather_list
        self.cloudy = ['сильный туман', 'дымка', 'облачность', 'малооблачно', 'туман', 'облачно']
        self.sunny = ['ясно']
        self.rain = ['слабый дождь', 'ливневая крупа', 'ливневый дождь', 'пасмурно', 'дождь']
        self.snow = ['ливневый снег', 'слабый снег', 'снег']
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

    def draw_background(self, x, y, z, x_draw, y_draw, z_draw, x_gradient, y_gradient, z_gradient, image):
        for width_pixel in range(self.width):
            if width_pixel in range(150):
                cv2.line(self.image, (width_pixel, 0), (width_pixel, self.height), (x, y, z), 1)
            elif width_pixel >= 150:
                if x > x_draw:
                    x -= x_gradient
                if y > y_draw:
                    y -= y_gradient
                if z > z_draw:
                    z -= z_gradient
                cv2.line(self.image, (width_pixel, 0), (width_pixel, self.height), (x, y, z), 1)
        self.image[60: 160, 20: 120] = image

    def draw_cloudy(self, image_draw):
        x_draw, y_draw, z_draw = 100, 100, 100
        x_gradient, y_gradient, z_gradient = 1, 1, 1
        self.draw_background(BGR_B, BGR_G, BGR_R, x_draw, y_draw, z_draw,
                             x_gradient, y_gradient, z_gradient, image_draw)

    def draw_rain(self, image_draw):
        x_draw, y_draw, z_draw = 230, 0, 0
        x_gradient, y_gradient, z_gradient = 1, 2, 2
        self.draw_background(BGR_B, BGR_G, BGR_R, x_draw, y_draw, z_draw,
                             x_gradient, y_gradient, z_gradient, image_draw)

    def draw_snow(self, image_draw):
        x = BGR_B - 9
        y = BGR_G - 9
        z = BGR_R - 9
        x_draw, y_draw, z_draw = x, 200, 125
        x_gradient, y_gradient, z_gradient = 0, 1, 2
        self.draw_background(x, y, z, x_draw, y_draw, z_draw,
                             x_gradient, y_gradient, z_gradient, image_draw)

    def draw_sun(self, image_draw):
        x_draw, y_draw, z_draw = 15, 220, BGR_R
        x_gradient, y_gradient, z_gradient = 2, 1, 0
        self.draw_background(BGR_B, BGR_G, BGR_R, x_draw, y_draw, z_draw,
                             x_gradient, y_gradient, z_gradient, image_draw)

    def draw_degree(self, degree_number, indent):
        if degree_number == '0':
            degree_celsius_text = 'градусов Цельсия'
        elif int(degree_number[1:]) in range(10, 21):
            degree_celsius_text = 'градусов Цельсия'
        elif int(degree_number[-1]) == 1:
            degree_celsius_text = 'градус Цельсия'
        elif int(degree_number[-1]) in range(2, 5):
            degree_celsius_text = 'градуса Цельсия'
        else:
            degree_celsius_text = 'градусов Цельсия'
        degrees_text = f'{degree_number} {degree_celsius_text}'
        self.draw_text(degrees_text, indent)

    def draw_image(self, weather_data):
        weather_funcs = {
            tuple(self.cloudy): (self.draw_cloudy, self.cloud_image),
            tuple(self.rain): (self.draw_rain, self.rain_image),
            tuple(self.snow): (self.draw_snow, self.snow_image),
            tuple(self.sunny): (self.draw_sun, self.sun_image)
        }

        for wf in weather_funcs:
            for weather_name in wf:
                if weather_name in weather_data['weather_for_the_day']:
                    func, img = weather_funcs[wf]
                    func(img)
                    self.draw_current_weather(weather_name)

        os.makedirs(FILES_IMAGE, exist_ok=True)

        self.draw_text('Температура:', 0)
        self.draw_text('днем', 50)
        self.draw_degree(weather_data['daytime_temperature'], 80)
        self.draw_text('ночью', 130)
        self.draw_degree(weather_data['night_temperature'], 160)
        self.draw_text_date(weather_data['date'].strftime('%d.%m.%Y'))



