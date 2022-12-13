import bpy
from .utils import filter_morphs

def load(object):
    if 'proportion_morphs' not in object:
        object['proportion_morphs'] = filter_morphs('Proportion', object)

    if 'body_morphs' not in object:
        exclude = ['Proportion', 'Mass']
        object['body_morphs'] = filter_morphs('Body', object, exclude)

    if 'mass_morphs' not in object:
        object['mass_morphs'] = filter_morphs('Mass', object)