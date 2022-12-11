import bpy

class UI_age_panel(bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_age_panel'
    bl_label = 'Age'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Human Artisan'
    
    def draw(self, context):
        layout = self.layout

        row = layout.row(align = True)
        row.operator("render.render") # Male
        row.operator("render.render") # Female

        row = layout.row()
        row.scale_x = 0.5
        row.operator("render.render") # Reset


# - - - - - - - - - - - - - - - - - - - - - - - -
# Export
# - - - - - - - - - - - - - - - - - - - - - - - -
def get():
    return (UI_age_panel, )
 