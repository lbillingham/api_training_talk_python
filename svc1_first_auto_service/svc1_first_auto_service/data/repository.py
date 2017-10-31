import csv
import os
import uuid

class Repository(object):
    __car_data = {}

    @classmethod
    def all_cars(cls, limit=None):
        cls.__load_data()
        cars = list(cls.__car_data.items())
        if limit:
            cars = cars[:limit]
        return cars

    @classmethod
    def car_by_id(cls, car_id):
        cls.__load_data()
        return cls.__car_data.get(car_id)

    @classmethod
    def __load_data(cls):
        if cls.__car_data:
            return
        filename = os.path.join(
            os.path.dirname(__file__),
            'opel.csv'
        )
        with open(filename, 'r', encoding='utf-8') as fin:
            # brand, model, price, year, damage, last_seen
            reader = csv.DictReader(fin)
            for row in reader:
                key = str(uuid.uuid4())
                row['id'] = key
                cls.__car_data[key] = row
