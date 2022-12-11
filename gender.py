import bpy
import re

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_gender_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_gender_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Human Artisan'
    bl_label = 'Gender'
    
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("object.male_shape_loader")
        row.operator("object.female_shape_loader")

        row = layout.row()
        row.operator("object.reset_gender_shape")


# - - - - - - - - - - - - - - - - - - - - - - - -
# Functions
# - - - - - - - - - - - - - - - - - - - - - - - -
def get_shape_key(name):
    active = bpy.context.view_layer.objects.active
    _type = active.type
    if _type == 'MESH':
        isG9F = re.search('Genesis9', active.data.name)
        if isG9F:
            return active.data.shape_keys.key_blocks.get(name)

def reset_shapes(ls):
    for sk in ls:
        sk = get_shape_key(sk)
        if sk: sk.value = 0


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class MaleShapeLoader(bpy.types.Operator):
    bl_idname = 'object.male_shape_loader'
    bl_label = 'Male'

    def execute(self, context):
        reset_shapes(['Base Masculine', 'Base Feminine'])
        shape_key = get_shape_key('Base Masculine')
        if shape_key: shape_key.value = 1

        return {'FINISHED'}

class FemaleShapeLoader(bpy.types.Operator):
    bl_idname = 'object.female_shape_loader'
    bl_label = 'Female'

    def execute(self, context):
        reset_shapes(['Base Masculine', 'Base Feminine'])
        shape_key = get_shape_key('Base Feminine')
        if shape_key: shape_key.value = 1

        return {'FINISHED'}

class ResetGenderShape(bpy.types.Operator):
    bl_idname = 'object.reset_gender_shape'
    bl_label = 'Reset'

    def execute(self, context):
        reset_shapes(['Base Masculine', 'Base Feminine'])
        
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
 