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