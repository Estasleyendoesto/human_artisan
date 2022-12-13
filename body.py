import bpy
from .utils import figure_active, reset_morphs

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_body_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Artisan'
    bl_label = 'Body'
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return figure_active()

    def draw(self, context):
        pass

class Body_head_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_body_panel'
    bl_parent_id = 'MAIN_PT_proportion_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Body'
    bl_options = {'HIDE_HEADER'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Proportion Height', 
            'Proportion Larger', 
            'Proportion Smaller', 
            'Proportion Smaller Body Only',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, text=name.replace('Proportion ', ''), slider=True)


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class ResetBodyMorph(bpy.types.Operator):
    bl_idname = 'object.reset_body_morph'
    bl_label = 'Reset'

    def execute(self, context):
        figure = figure_active()
        reset_morphs(figure['body_morphs'])
        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_body_panel,
    ResetBodyMorph,
)