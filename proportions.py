import bpy
from .utils import figure_active, reset_morphs

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_proportion_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_proportion_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Artisan'
    bl_label = 'Proportions'
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return figure_active()

    def draw(self, context):
        pass

class Proportion_body_panel(bpy.types.Panel):
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

class Proportion_torso_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_torso_panel'
    bl_parent_id = 'MAIN_PT_proportion_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Torso'
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Proportion Head Size', 
            'Proportion Neck Length', 
            'Proportion Shoulder Height', 
            'Proportion Shoulder Width', 
            'Proportion Chest Depth', 
            'Proportion Chest Width', 
            'Proportion Chest Volume', 
            'Proportion Torso Length',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, text=name.replace('Proportion ', ''), slider=True)

class Proportion_arms_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_arms_panel'
    bl_parent_id = 'MAIN_PT_proportion_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Arms'
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Proportion Arms Length',
            'Proportion Hand Size',
            'Proportion Palm Size',
            'Proportion Fingers Length',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, text=name.replace('Proportion ', ''), slider=True)

class Proportion_legs_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_legs_panel'
    bl_parent_id = 'MAIN_PT_proportion_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Legs'
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Proportion Legs Length',
            'Proportion Foot Size',
            'Proportion Foot Length',
            'Proportion Toes Length',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, text=name.replace('Proportion ', ''), slider=True)

class Proportion_reset_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_reset_panel'
    bl_parent_id = 'MAIN_PT_proportion_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Reset'
    bl_options = {'HIDE_HEADER'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('object.reset_proportion_morph')


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class ResetProportionMorph(bpy.types.Operator):
    bl_idname = 'object.reset_proportion_morph'
    bl_label = 'Reset'

    def execute(self, context):
        figure = figure_active()
        reset_morphs(figure['proportion_morphs'])
        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_proportion_panel,
    Proportion_body_panel,
    Proportion_torso_panel,
    Proportion_arms_panel,
    Proportion_legs_panel,
    ResetProportionMorph,
    Proportion_reset_panel,
)
 