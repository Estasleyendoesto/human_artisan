# - - - - - - - - - - - - - - - - - - - - - - - -
# Functions
# - - - - - - - - - - - - - - - - - - - - - - - -
import bpy
import re

def figure_active():
    active = bpy.context.view_layer.objects.active
    if active is None: 
        return
    _type = active.type
    if _type == 'MESH':
        isG9F = re.search('Genesis9', active.data.name)
        if isG9F:
            return active

def get_morph_value(name):
    object = figure_active()
    if object:
        return object.get(name)

def update_morph(name, value):
    object = figure_active()
    if object:
        object[name] = value
        object.data.update()

def reset_morphs(ls):
    for morph in ls:
        update_morph(morph, 0.0)

def filter_morphs(str, object=None, exclude=[]):
    morphs = []
    if not object:
        object = figure_active()
    if object:
        for i in object.keys():
            # Exclusion
            times = 0
            for w in exclude:
                exc = re.search(w, i)
                if exc:
                    times += 1
            if times:
                continue
            # No coincidences
            else:
                prop = re.search(str, i)
                if prop:
                    morphs.append(i)  
    return morphs