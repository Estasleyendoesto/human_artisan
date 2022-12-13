import bpy
from .utils import filter_morphs

def load(object):
    if 'proportion_morphs' not in object:
        object['proportion_morphs'] = filter_morphs('Proportion', object)

    if 'fullbody_morphs' not in object:
        exclude = ['Proportion', 'Mass']
        object['fullbody_morphs'] = filter_morphs('Body', object, exclude)

    if 'mass_morphs' not in object:
        object['mass_morphs'] = filter_morphs('Mass', object)

    if 'taper_morphs' not in object:
        object['taper_morphs'] = filter_morphs('Taper', object)