bl_info = {
    "name": "Human Artisan",
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

from . import setup, gender, age
classes = setup.cls + gender.cls

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    del bpy.types.WindowManager.isLoaded

if __name__ == '__main__':
    register()
    
print("Human Artisan loaded")