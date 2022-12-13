import bpy
from .utils import figure_active, reset_morphs

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_taper_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_taper_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Artisan'
    bl_label = 'Taper'
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return figure_active()

    def draw(self, context):
        layout = self.layout        
        figure = figure_active()
        for name in figure['taper_morphs']:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, text=name.replace('Taper ', ''), slider=True)

        row = layout.row()
        row.operator('object.reset_taper_morph')


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class ResetTaperMorph(bpy.types.Operator):
    bl_idname = 'object.reset_taper_morph'
    bl_label = 'Reset'

    def execute(self, context):
        figure = figure_active()
        reset_morphs(figure['taper_morphs'])
        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_taper_panel,
    ResetTaperMorph,
)
 