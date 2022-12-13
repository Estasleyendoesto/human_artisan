import bpy
from .utils import figure_active, reset_morphs

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_asymmetry_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Artisan'
    bl_label = 'Asymmetry'
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return figure_active()

    def draw(self, context):
        pass

class Asymmetry_ears_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_ears_panel'
    bl_parent_id = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Ears'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Asymmetry Ears 01 Left',
            'Asymmetry Ears 01 Right',
            'Asymmetry Ears 02 Left',
            'Asymmetry Ears 02 Right',
            'Asymmetry Ears 03 Left',
            'Asymmetry Ears 03 Right',
            'Asymmetry Ears Position Height Left',
            'Asymmetry Ears Position Height Right',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Asymmetry_face_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_face_panel'
    bl_parent_id = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Face'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Asymmetry Face Heart Left',
            'Asymmetry Face Heart Right',
            'Asymmetry Face Round Left',
            'Asymmetry Face Round Right',
            'Asymmetry Face Square Left',
            'Asymmetry Face Square Right',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Asymmetry_brows_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_brows_panel'
    bl_parent_id = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Brows'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Asymmetry Brow Height Left',
            'Asymmetry Brow Height Right',
            'Asymmetry Brow Size  Left',
            'Asymmetry Brow Size Right',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Asymmetry_cheek_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_cheek_panel'
    bl_parent_id = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Cheek'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Asymmetry Cheek Size Left',
            'Asymmetry Cheek Size Right',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Asymmetry_jaw_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_jaw_panel'
    bl_parent_id = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Jaw'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Asymmetry Jaw Horizontal Balance',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Asymmetry_eyes_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_eyes_panel'
    bl_parent_id = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Eyes'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Asymmetry Eyes Angle Left',
            'Asymmetry Eyes Angle Right',
            'Asymmetry Eyes Position Depth Left',
            'Asymmetry Eyes Position Depth Right',
            'Asymmetry Eyes Position Height Left',
            'Asymmetry Eyes Position Height Right',
            'Asymmetry Eyes Position Width Left',
            'Asymmetry Eyes Position Width Right',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Asymmetry_eyelids_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_eyelids_panel'
    bl_parent_id = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Eyelids'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Asymmetry Eyelids Crease Height Left',
            'Asymmetry Eyelids Crease Height Right',
            'Asymmetry Eyelids Lower Relax Left',
            'Asymmetry Eyelids Lower Relax Right',
            'Asymmetry Eyelids Upper Relax Left',
            'Asymmetry Eyelids Upper Relax Right',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Asymmetry_mouth_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_mouth_panel'
    bl_parent_id = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Mouth'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Asymmetry Mouth Angle Left',
            'Asymmetry Mouth Angle Right',
            'Asymmetry Mouth Mid Curve Left',
            'Asymmetry Mouth Mid Curve Right',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Asymmetry_lips_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_lips_panel'
    bl_parent_id = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Lips'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Asymmetry Lip Lower Thickness Left',
            'Asymmetry Lip Lower Thickness Right',
            'Asymmetry Lip Upper Thickness Left',
            'Asymmetry Lip Upper Thickness Right',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Asymmetry_nose_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_nose_panel'
    bl_parent_id = 'MAIN_PT_asymmetry_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Nose'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Asymmetry Nose Base Horizontal',
            'Asymmetry Nose Base Twist',
            'Asymmetry Nose Bridge Upper Horizontal',
            'Asymmetry Nose Bridge Horizontal',
            'Asymmetry Nose Rotate Left',
            'Asymmetry Nose Rotate Right',
            'Asymmetry Nose Tip Balance Left',
            'Asymmetry Nose Tip Balance Right',
            'Asymmetry Nose Wing Height Porision Left',
            'Asymmetry Nose Wing Height Position Right',
            'Asymmetry Nose Wing Size Left',
            'Asymmetry Nose Wing Size Right',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_asymmetry_panel,
    Asymmetry_brows_panel,
    Asymmetry_cheek_panel,
    Asymmetry_ears_panel,
    Asymmetry_eyelids_panel,
    Asymmetry_eyes_panel,
    Asymmetry_jaw_panel,
    Asymmetry_lips_panel,
    Asymmetry_face_panel,
    Asymmetry_nose_panel,
    Asymmetry_mouth_panel,
)