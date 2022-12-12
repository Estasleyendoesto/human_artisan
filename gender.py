import bpy
from .utils import *

# - - - - - - - - - - - - - - - - - - - - - - - -
# Data
# - - - - - - - - - - - - - - - - - - - - - - - -
shapes = (
    'Base Masculine',
    'Base Feminine',
)

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_gender_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_gender_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Artisan'
    bl_label = 'Gender'

    @classmethod
    def poll(cls, context):
        return figure_active()
    
    def draw(self, context):
        obj = figure_active()
        layout = self.layout

        row = layout.row()
        row.operator("object.male_shape_loader",   depress=True if obj[shapes[0]] != 0 else False)
        row.operator("object.female_shape_loader", depress=True if obj[shapes[1]] != 0 else False)

        row = layout.row()
        row.operator("object.reset_gender_shape")
        

# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class MaleShapeLoader(bpy.types.Operator):
    bl_idname = 'object.male_shape_loader'
    bl_label = 'Male'

    def execute(self, context):
        reset_morphs(shapes)
        update_morph(shapes[0], 1)
        return {'FINISHED'}

class FemaleShapeLoader(bpy.types.Operator):
    bl_idname = 'object.female_shape_loader'
    bl_label = 'Female'

    def execute(self, context):
        reset_morphs(shapes)
        update_morph(shapes[1], 1)
        return {'FINISHED'}

class ResetGenderShape(bpy.types.Operator):
    bl_idname = 'object.reset_gender_shape'
    bl_label = 'Reset'

    def execute(self, context):
        reset_morphs(shapes)
        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_gender_panel, 
    MaleShapeLoader,
    FemaleShapeLoader,
    ResetGenderShape,
)
 