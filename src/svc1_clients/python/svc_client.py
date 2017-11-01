from pprint import pprint
import requests


def main():
    cars = list_cars()
    show_cars(cars)

    car_id = input('What car do you want to see (car ID): ')
    show_car_details(car_id)


def show_car_details(car_id):
    car = get_car(car_id)
    pprint(car)


def show_cars(cars):
    print('Cars for sale:')
    for c in cars:
        print(f'{c[0]}: {c[1]}')


def get_car(car_id):
    url = f'http://localhost:6543/api/autos/{car_id}'
    response = requests.get(url)
    response.raise_for_status()
    car = response.json()
    return car


def list_cars():
    url = 'http://localhost:6543/api/autos'
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        print(f'ERROR contacting server status: {response.status_code}')
    cars = response.json()
    return [
        (car.get('id'), car.get('name'))
        for car in cars
]


if __name__ == '__main__':
    main()
