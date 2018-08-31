_auther_ = 'Harry'
_date_ = '7/26/2018 6:51 PM'

import os
from django.contrib.gis.utils import LayerMapping
from .models import Countie

countie_mapping = {
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}

countie_shp =  os.path.abspath(os.path.join(os.path.dirname(__file__),'data/counties.shp'))

def run(verbose = True):
    lm = LayerMapping(Countie,countie_shp,countie_mapping,transform=False,encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)

