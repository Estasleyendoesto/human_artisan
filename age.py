import bpy
from .utils import figure_active, reset_morphs

# - - - - - - - - - - - - - - - - - - - - - - - -
# Data
# - - - - - - - - - - - - - - - - - - - - - - - -
shapes = (
    'Age 5 To 6 Years',
    'Age 9 To 10 Years',
    'Age Young Teen',
    'Age Older Teen',
)


# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_age_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_age_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Artisan'
    bl_label = 'Age'
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return figure_active()

    def draw(self, context):
        layout = self.layout
        for name in shapes:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, text=name.replace('Age ', ''), slider=True)

        row = layout.row()
        row.operator('object.reset_age_shape')


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class ResetAgeShape(bpy.types.Operator):
    bl_idname = 'object.reset_age_shape'
    bl_label = 'Reset'

    def execute(self, context):
        reset_morphs(shapes)
        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_age_panel,
    ResetAgeShape,
)
 