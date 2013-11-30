import re
import exceptions

from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import get_renderer
from pyramid.view import view_config

#from filterengine import FilterEngine


class GeoDiggerUI(object):
    def __init__(self, request):
        self.request = request
        renderer = get_renderer("templates/layout.pt")
        self.layout = renderer.implementation().macros['layout']

    @view_config(route_name='home',
            renderer='templates/home.pt',
            request_method='GET')
    def home_get(self):
        sliderOptions = str({
            'bounds': {
                'min': 'new Date(2012, 0, 1)',
                'max': 'new Date(2013, 11, 31)'
            },
            'defaultValues': {
                'min': 'new Date(2012, 0, 1)',
                'max': 'new Date(2013, 11, 31)'
            },
            'scales': [{
            'next': 'function(value){ var next = new Date(value); return new Date(next.setMonth(value.getMonth() + 1)); }',
            'label': 'function(value){ return months[value.getMonth()]; }',
            }],
        }).replace("'", '')
        return dict(title='Filter Parameters', sources=['Twitter'],
                sliderOptions=sliderOptions, error=None)

    @view_config(route_name='home',
            renderer='templates/home.pt',
            request_method='POST')
    def home_post(self):
        print self.request.params
        return dict(title='Filter Parameters', sources=['Twitter'],
                sliderOptions=None, error="Error: Not yet implemented.")
#        url = self.request.route_url('dns_addedit', hostname=hostname)
#        return HTTPFound(url)
