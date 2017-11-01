from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from svc1_first_auto_service.data.repository import Repository


@view_config(route_name='autos_api',
             request_method='GET',
             renderer='json')
def all_autos(_):
    cars = Repository.all_cars(limit=25)
    return cars


@view_config(route_name='autos_api',
             request_method='POST',
             renderer='json')
def add_auto(request: Request):
    try:
        car_data = request.json_body
    except Exception:  # woo broad
        return Response(status=400, body='Could not parse your post as JSON')
    # TODO: Validate
    try:
        car_data = Repository.add_car(car_data)
        return car_data
    except Exception as err:
        return Response(status=400, body=f'Could not save car {err}')


@view_config(route_name='auto_api',
             request_method='GET',
             renderer='json')
def single_auto(request: Request):
    car_id = request.matchdict.get('car_id')
    car = Repository.car_by_id(car_id)
    if not car:
        msg = f'car with id {car_id} was not found'
        return Response(status=404, json_body={'error': msg})
    return car
