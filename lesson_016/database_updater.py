from peewee import *

from weather_maker import WeatherMaker
import keys_db

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


class DatabaseUpdater:

    def __init__(self):
        self.wb = WeatherBase

    def save_data(self):

        db.connect()
        db.create_tables([self.wb])
        weather_maker = WeatherMaker()

        for row in weather_maker.get_forecast():
            weather_base = self.wb(date=row['date'],
                                   daytime_temperature=row['daytime_temperature'],
                                   night_temperature=row['night_temperature'],
                                   weather_for_the_day=row['weather_for_the_day'])
            weather_base.save()

    def get_data(self):
        for datawb in WeatherBase.select():
            print(datawb.date, datawb.daytime_temperature, datawb.night_temperature, datawb.weather_for_the_day)


if __name__ == '__main__':
    dbu = DatabaseUpdater()
    dbu.save_data()
    dbu.get_data()
