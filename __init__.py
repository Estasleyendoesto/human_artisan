bl_info = {
    "name": "Artisan",
    "author": "Estasleyendoesto",
    "version": (0, 1),
    "blender": (3, 3, 1),
    "location": "3D View > Sidebar > Human Artisan",
    "description": "Human Creator using Genesis 9 Morphs and more",
    "warning": "",
    "doc_url": "",
    "category": "Mesh",
}

import bpy
from . import fullbody, setup, gender, age, pose, proportions, mass, taper, body

def app():
    return setup.cls + gender.cls + age.cls + fullbody.cls + proportions.cls + taper.cls + mass.cls + body.cls + pose.cls

def register():
    for c in app():
        bpy.utils.register_class(c)

def unregister():
    for c in app():
        bpy.utils.unregister_class(c)

if __name__ == '__main__':
    register()