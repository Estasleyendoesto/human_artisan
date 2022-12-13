import bpy
from .utils import figure_active, reset_morphs

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_fullbody_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_fullbody_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Artisan'
    bl_label = 'Full Body'
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return figure_active()

    def draw(self, context):
        layout = self.layout        
        figure = figure_active()
        for name in figure['fullbody_morphs']:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, text=name.replace('Body ', ''), slider=True)

        row = layout.row()
        row.operator('object.reset_fullbody_morph')


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class ResetFullBodyMorph(bpy.types.Operator):
    bl_idname = 'object.reset_fullbody_morph'
    bl_label = 'Reset'

    def execute(self, context):
        figure = figure_active()
        reset_morphs(figure['fullbody_morphs'])
        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_fullbody_panel,
    ResetFullBodyMorph,
)
 