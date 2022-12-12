import bpy
from .utils import figure_active, reset_morphs

# - - - - - - - - - - - - - - - - - - - - - - - -
# Data
# - - - - - - - - - - - - - - - - - - - - - - - -
shapes = (
    'Pose Closed Arms',
    'Pose Closed Legs',
    'Pose Chest Front',
    'Pose Jumping',
    'Pose Kneeling',
    'Pose Running',
    'Pose Sitting',
    'Pose Yoga',
    'Pose 4',
    'Pose 4 Open',
)


# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_pose_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_pose_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Artisan'
    bl_label = 'Pose'
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        return figure_active()

    def draw(self, context):
        layout = self.layout
        for name in shapes:
            row = layout.row(align = True)
            row.prop(context.object, '["%s"]' % name, text=name.replace('Pose ', ''), slider=True)

        row = layout.row()
        row.operator('object.reset_pose_morph')


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class ResetPoseMorph(bpy.types.Operator):
    bl_idname = 'object.reset_pose_morph'
    bl_label = 'Reset'

    def execute(self, context):
        reset_morphs(shapes)
        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_pose_panel,
    ResetPoseMorph,
)
 