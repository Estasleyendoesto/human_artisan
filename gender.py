import bpy

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
        row.operator("object.male_shape_loader") # Male
        row.operator("object.female_shape_loader") # Female

        row = layout.row()
        row.operator("object.reset_gender_shape") # Reset


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class MaleShapeLoader(bpy.types.Operator):
    bl_idname = 'object.male_shape_loader'
    bl_label = 'Male'

    def execute(self, context):
        print('Male Shape loaded')

        return {'FINISHED'}

class FemaleShapeLoader(bpy.types.Operator):
    bl_idname = 'object.female_shape_loader'
    bl_label = 'Female'

    def execute(self, context):
        print('Female Shape loaded')

        return {'FINISHED'}

class ResetGenderShape(bpy.types.Operator):
    bl_idname = 'object.reset_gender_shape'
    bl_label = 'Reset'

    def execute(self, context):
        print('Reset gender shape')

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
 