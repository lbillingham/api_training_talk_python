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
             request_method='POST')
def add_auto(request: Request):
    try:
        car_data = request.json_body
    except Exception:  # woo broad
        return Response(status=400, body='Could not parse your post as JSON')
    # TODO: Validate
    try:
        car_data = Repository.add_car(car_data)
        return Response(status=201, json_body=car_data)
    except Exception as err:
        return Response(status=500, body=f'Could not save car {err}')


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


@view_config(route_name='auto_api',
             request_method='PUT')
def update_auto(request: Request):
    car_id = request.matchdict.get('car_id')
    if not Repository.car_by_id(car_id):
        msg = f'car with id {car_id} was not found'
        return Response(status=404, json_body={'error': msg})
    try:
        new_data = request.json_body
    except Exception as err:  # woo broad
        return Response(status=400, body='Could not parse your put as JSON')
    # TODO: Validate
    try:
        Repository.update_car(car_id, new_data)
        return Response(status=204, body=f'car: {car_id} updated successfully')
    except Exception as err:
        return Response(status=500, body=f'Could not update car: {car_id} because {err}')


@view_config(route_name='auto_api',
             request_method='DELETE')
def delete_auto(request: Request):
    car_id = request.matchdict.get('car_id')
    car = Repository.car_by_id(car_id)
    if not car:
        msg = f'car with id {car_id} was not found'
        return Response(status=404, json_body={'error': msg})
    try:
        Repository.delete_car(car_id)
        return Response(status=204, body=f'car {car_id} deleted successfully')
    except Exception as err:
        return Response(status=500, body=f'Could not delete car: {car_id} because {err}')