from pyramid.view import view_config


@view_config(route_name='autos_api',
             request_method='GET',
             renderer='json')
def all_autos(_):
    return {'test': 'was autos'}

@view_config(route_name='auto_api',
             request_method='GET',
             renderer='json')
def single_auto(request):
    return {'test': 'is auto'}