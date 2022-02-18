from xmlrpc.client import Marshaller


planet={
    'name': 'Mars',
    'moons': 2
}
print(f'{planet["name"]} has {planet["moons"]} moons')

planet['circunferencia (km)']={
    'polar':6752,
    'equatorial': 6792
}
print(f'{planet["name"]} has a polar circunferencia of {planet["circunferencia (km)"]["polar"]}')
