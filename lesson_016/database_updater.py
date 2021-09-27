from peewee import *

from weather_maker import WeatherMaker
import keys_db

NAMES_TABLE = ['date', 'daytime_temperature', 'night_temperature', 'weather_for_the_day']

db = PostgresqlDatabase(database=keys_db.DATABASE,
                        user=keys_db.USER,
                        password=keys_db.PASSWORD,
                        host=keys_db.HOST,
                        port=keys_db.PORT)


class BaseModel(Model):
    class Meta:
        database = db


class WeatherBase(BaseModel):
    date = DateTimeField()
    daytime_temperature = CharField()
    night_temperature = CharField()
    weather_for_the_day = CharField()


lst = [WeatherBase.date, WeatherBase.daytime_temperature,
       WeatherBase.night_temperature, WeatherBase.weather_for_the_day]


class DatabaseUpdater:

    def __init__(self):
        self.wb = WeatherBase
        self.weather_list = []

    def save_data(self):

        db.connect()
        db.create_tables([self.wb])
        weather_maker = WeatherMaker()

        for row in weather_maker.get_forecast():
            weather_base = self.wb(date=row[NAMES_TABLE[0]],
                                   daytime_temperature=row[NAMES_TABLE[1]],
                                   night_temperature=row[NAMES_TABLE[2]],
                                   weather_for_the_day=row[NAMES_TABLE[3]])
            weather_base.save()

    def get_data(self):
        for datawb in WeatherBase.select():
            self.weather_list.append({
                NAMES_TABLE[0]: datawb.date,
                NAMES_TABLE[1]: datawb.daytime_temperature,
                NAMES_TABLE[2]: datawb.night_temperature,
                NAMES_TABLE[3]: datawb.weather_for_the_day})
        return self.weather_list

