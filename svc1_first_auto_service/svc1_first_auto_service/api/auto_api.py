from pyramid.request import Request, Response
from pyramid.view import view_config

from svc1_first_auto_service.data.repository import Repository


@view_config(route_name='autos_api',
             request_method='GET',
             renderer='json')
def all_autos(_):
    cars = Repository.all_cars(limit=25)
    return cars

@view_config(route_name='auto_api',
             request_method='GET',
             renderer='json')
def single_auto(request):
    car_id = request.matchdict.get('car_id')
    car = Repository.car_by_id(car_id)
    if not car:
        msg = f'car with id {car_id} was not found'
        return Response(status=404, json_body={'error': msg})
    return car
