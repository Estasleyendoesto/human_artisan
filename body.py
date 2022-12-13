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

class Body_neck_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_neck_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Neck'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Jaw to Neck Slack', 
            'Neck Shape Back', 
            'Neck Shape Front', 
            'Collarbone Detail',
            'Collarbone Mid Shape',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_back_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_back_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Back'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Shoulder Blades', 
            'Lats Size', 
            'Spine', 
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_arms_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_arms_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Arms'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Arms Muscular', 
            'Arms Volume', 
            'Fingers Width', 
            'Nails Length Round', 
            'Nails Length Sharp', 
            'Nails Length Square', 
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_breasts_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_breasts_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Breasts'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Breasts Bigger',
            'Breasts Large High',
            'Breasts Large',
            'Breasts Heavy',
            'Breasts Natural',
            'Breasts Small',
            'Breasts Gone',
            'Breasts Reduction',
            'Breasts Cleavage',
            'Breasts Perk Side',
            'Breasts Diameter',
            'Breasts Downward Slope',
            'Breasts Slope',
            'Breasts Fullness Lower',
            'Breasts Fullness Upper',
            'Breasts Under Curve',
            'Breasts Sides Depth',
            'Breasts Shape 01',
            'Breasts Shape 02',
            'Breasts Shape 03',
            'Breasts Shape 04',
            'Breasts Shape 05',
            'Breasts Shape 06',
            'Breasts Shape 07',
            'Breasts Shape 08',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_nipples_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_nipples_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Nipples'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Nipples Areolae Diameter Feminine',
            'Nipples Areolae Diameter Masculine',
            'Nipples Areolae Depth Feminine',
            'Nipples Areolae Depth Masculine',
            'Nipples Depth Feminine HD',
            'Nipples Depth Masculine HD',
            'Nipples Diameter Feminine',
            'Nipples Diameter Masculine',
            'Nipples Feminine HD',
            'Nipples Masculine HD',
            'Nipples Tips Feminine Large HD',
            'Nipples Tips Masculine Large HD',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_torso_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_torso_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Torso'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Havel Size HD',
            'Stomach Depth',
            'Stomach Soften',
            'Abdominals Width',
            'Abdominals Center Define',
            'Abdominals Outer Define',
            'Navel Depth',
            'Navel HD',
            'Navel Horizontal HD',
            'Navel Vertical HD',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_waist_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_waist_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Waist'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Waist Depth',
            'Waist Width Upper',
            'Waist Width',
            'Love Handles',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_hip_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_hip_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Hip'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Hip Size',
            'Hip Pelvic Tilt',
            'Hip Bone Size',
            'Hip Bone Crest',
            'Hip Back Dimples',
            'Hip V Define',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_crotch_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_crotch_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Crotch'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Anatomy Area Height',
            'Anatomy Area Width',
            'Anatomy Groin Crease',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_glutes_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_glutes_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Glutes'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Glute Size',
            'Glute Width',
            'Glute Crease',
            'Glute Depth Upper',
            'Glute Depth Lower',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_legs_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_legs_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Legs'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Legs Lower Volume',
            'Legs Upper Back Shape',
            'Legs Upper Front Shape',
            'Legs Upper Volume',
            'Legs Volume',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_thigh_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_thigh_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Thigh'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Thigh Depth',
            'Thigh Inner 1',
            'Thigh Inner 2',
            'Thigh Length',
            'Thigh Outer',
            'Thigh Tone',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_knee_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_knee_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Knee'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Knee Bones Size',
            'Knee Detail Front ',
            'Knee Detail Rear',
            'Knee Inner',
            'Knee Outer',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_calf_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_calf_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Calf'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Calf Height',
            'Calf Rotate',
            'Calves Size',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_shin_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_shin_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Shin'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Shin Bone',
            'Shin Length',
            'Shin Thickness',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_ankle_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_ankle_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Ankle'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Ankle Shape',
            'Ankle Thickness',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_feet_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_feet_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Feet'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Feet Dorsum Shape',
            'Feet Soles Shape',
            'Foot Arch Depth',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Body_toes_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_toes_panel'
    bl_parent_id = 'MAIN_PT_body_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Toes'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Big Toe Length',
            'Index Toe Length',
            'Mid Toe Length',
            'Pinky Toe Length',
            'Ring Toe Length',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_body_panel,
    Body_neck_panel,
    Body_back_panel,
    Body_arms_panel,
    Body_torso_panel,
    Body_waist_panel,
    Body_hip_panel,
    Body_crotch_panel,
    Body_glutes_panel,
    Body_legs_panel,
    Body_thigh_panel,
    Body_knee_panel,
    Body_calf_panel,
    Body_shin_panel,
    Body_ankle_panel,
    Body_toes_panel,
    Body_feet_panel,
    Body_breasts_panel,
    Body_nipples_panel,
)