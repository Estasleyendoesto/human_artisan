import bpy
from .utils import filter_morphs

def load(object):
    if 'proportion_morphs' not in object:
        object['proportion_morphs'] = filter_morphs('Proportion', object)