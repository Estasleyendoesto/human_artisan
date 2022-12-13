import bpy
from .utils import figure_active

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_head_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Artisan'
    bl_label = 'Head'
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return figure_active()

    def draw(self, context):
        pass

class Head_cranium_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_cranium_panel'
    bl_parent_id = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Cranium'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Cranium Size',
            'Cranium Height',
            'Cranium Slope',
            'Skull Size',
            'Skull Width',
            'Skull Above Ear Width',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Head_ears_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_ears_panel'
    bl_parent_id = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Ears'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Ear Elf',
            'Ear Elf Long',
            'Ear Depth',
            'Ear Height',
            'Ear Size Upper',
            'Ear Size Lower',
            'Ear Attached',
            'Earlobe Length',
            'Earlobe Size',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Head_face_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_face_panel'
    bl_parent_id = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Face'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Face Angle',
            'Face Center Depth',
            'Face Depth',
            'Face Flat',
            'Face Heart',
            'Face Older',
            'Face Round',
            'Face Size',
            'Face Square',
            'Face Young',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Head_brows_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_brows_panel'
    bl_parent_id = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Brows'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Brow Above Depth Inner',
            'Brow Above Depth Outer',
            'Brow Arch Size Inner',
            'Brow Arch Size Outer',
            'Brow Sharpen',
            'Brow Skin Slack',
            'Brow Temple Narrow',
            'Brow Whole Height',
            'Brow Whole Size',
            'Brow Whole Width',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Head_cheek_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_cheek_panel'
    bl_parent_id = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Cheek'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Cheek Crease Depth',
            'Cheek Lower Size',
            'Cheek Middle Diagonal Bisect',
            'Cheel Middle Size',
            'Cheek Sink',
            'Cheek Size',
            'Cheek Tear Trough',
            'Cheek to Jaw Size',
            'Cheek to Lip Depth',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Head_chin_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_chin_panel'
    bl_parent_id = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Chin'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Chin Cleft',
            'Chin Depth',
            'Chin Height',
            'Chin to Lip Depth',
            'Chin to Lip Sharpen',
            'Chin to Width',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Head_jaw_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_jaw_panel'
    bl_parent_id = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Jaw'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Jaw Middle Curve',
            'Jaw Rear Height',
            'Jaw Rear Width',
            'Jaw Whole Height',
            'Jaw Whole Sharpen',
            'Jaw Whole Size',
            'Jaw Whole Width',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Head_mouth_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_mouth_panel'
    bl_parent_id = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Mouth'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Mouth Depth',
            'Mouth Size',
            'Mouth Height',
            'Mouth Width',
            'Mouth Realism',
            'Mouth Above Size Inner',
            'Mouth Above Size Outer',
            'Mouth Aperture Curve',
            'Mouth Below Hollow',
            'Mouth Below Size Inner',
            'Mouth Below Size Outer',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)    

class Head_nose_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_nose_panel'
    bl_parent_id = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Nose'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Nose Base Angle',
            'Nose Flesh Size',
            'Nose Base Height',
            'Nose Base Pinched',
            'Nose Base Size',
            'Nose Whole Size',
            'Nose Whole Width',
            'Nose Whole Depth',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Nose_shapes_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_shapes_panel'
    bl_parent_id = 'SUB_PT_head_nose_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Shapes'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Nose African',
            'Nose Bulbous',
            'Nose Define',
            'Nose Greek',
            'Nose Hawk',
            'Nose Model',
            'Nose Nubian',
            'Nose Roman',
            'Nose Snubbed',
            'Nose Straight',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Nose_bridge_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_bridge_panel'
    bl_parent_id = 'SUB_PT_head_nose_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Bridge'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Nose Bridge Bump',
            'Nose Bridge Definition',
            'Nose Bridge Depth',
            'Nose Bridge Size',
            'Nose Bridge Slope',
            'Nose Bridge to Cheek Depth',
            'Nose Bridge Width',
            'Nose Bridge Upper Depth',
            'Nose Bridge Upper Height',
            'Nose Bridge Upper Hollow',
            'Nose Bridge Upper Size',
            'Nose Bridge Upper Width',
            'Nose Bridge Lower Slope',
            'Nose Bridge Lower Width',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Nose_tip_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_tip_panel'
    bl_parent_id = 'SUB_PT_head_nose_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Tip'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Nose Tip Depth',
            'Nose Tip Height',
            'Nose Tip Septum Contour',
            'Nose Tip Size',
            'Nose Tip Upturn',
            'Nose Tip Width',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Nose_wing_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_wing_panel'
    bl_parent_id = 'SUB_PT_head_nose_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Wing'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Nose Wing Depth',
            'Nose Wing Height',
            'Nose Wing Lower Height',
            'Nose Wing Lower Width',
            'Nose Wing Size',
            'Nose Wing Size Vertical',
            'Nose Wing Width',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Nose_philtrum_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_philtrum_panel'
    bl_parent_id = 'SUB_PT_head_nose_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Philtrum'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Nose Philtrum Angle',
            'Nose Philtrum Center Depth',
            'Nose Philtrum Outer Depth',
            'Nose Philtrum Width',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Head_eyes_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_eyes_panel'
    bl_parent_id = 'MAIN_PT_head_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Eyes'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Eyes Almond',
            'Eyes Downturned',
            'Eyes Droop',
            'Eyes Hooded',
            'Eyes Narrow',
            'Eyes Round',
            'Eyes Upturned',
            'Eyes Distance',
            'Eyes Size',
            'Eyes Up / Down',
            'Eye Almond Inner',
            'Eye Almond Outer',
            'Eye Angle Inner',
            'Eye Angle Outer',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Eyes_eyelidUpper_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_eyelidUpper_panel'
    bl_parent_id = 'SUB_PT_head_eyes_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Eyelid Upper'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Eyelid Angle Upper Outer',
            'Eyelid Crease Upper Inner Height',
            'Eyelid Crease Upper Outer Height',
            'Eyelid Crease Upper Smooth',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Eyes_eyelidLower_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_eyelidLower_panel'
    bl_parent_id = 'SUB_PT_head_eyes_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Eyelid Lower'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Eye Socket Lower Depth',
            'Eye Socket Puffy Lower',
            'Eyelid Angle Lower Outer',
            'Eyelid Crease Lower Deepen',
            'Eyelid Crease Lower Height',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)

class Eyes_lacrimal_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_head_lacrimal_panel'
    bl_parent_id = 'SUB_PT_head_eyes_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Lacrimal'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        morphs = (
            'Lacrimal Inner Height',
            'Lacrimal Pinch',
            'Lacrimal Size',
            'Lacrimal Shape',
            'Lacrimal Fleshy',
        )
        for name in morphs:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, slider=True)


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_head_panel,
    Head_cranium_panel,
    Head_ears_panel,
    Head_brows_panel,
    Head_cheek_panel,
    Head_chin_panel,
    Head_eyes_panel,
    Head_face_panel,
    Head_jaw_panel,
    Head_mouth_panel,
    Head_nose_panel,
    Nose_bridge_panel,
    Nose_philtrum_panel,
    Nose_shapes_panel,
    Nose_tip_panel,
    Nose_wing_panel,
    Eyes_eyelidLower_panel,
    Eyes_eyelidUpper_panel,
    Eyes_lacrimal_panel,
)