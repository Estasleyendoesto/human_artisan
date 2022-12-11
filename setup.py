import bpy

# - - - - - - - - - - - - - - - - - - - - - - - -
# Panels
# - - - - - - - - - - - - - - - - - - - - - - - -
class UI_setup_panel(bpy.types.Panel):
    bl_idname = 'MAIN_PT_setup_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Human Artisan'
    bl_label = 'Setup (0.1)'

    def draw(self, context):
        pass
    
class Setup_load_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_load_panel'
    bl_parent_id = 'MAIN_PT_setup_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Load'
    bl_options = {'HIDE_HEADER'}
    
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('object.figure_loader')

class Setup_utils_panel(bpy.types.Panel):
    bl_idname = 'SUB_PT_utils_panel'
    bl_parent_id = 'MAIN_PT_setup_panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Utils'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.scene_loader")
        
        row = layout.row()
        row.operator("object.render_settings_loader")

        row = layout.row()
        row.operator("object.reset_all")

        


# - - - - - - - - - - - - - - - - - - - - - - - -
# Operators
# - - - - - - - - - - - - - - - - - - - - - - - -
class FigureLoader(bpy.types.Operator):
    bl_idname = 'object.figure_loader'
    bl_label = 'Load Figure'

    def execute(self, context):
        import os
        path = os.path.dirname(os.path.abspath(__file__)) + r'\base.blend'
        
        objects_to_append = ['Genesis 9']
        with bpy.data.libraries.load(path) as (data_from, data_to):
            data_to.objects = [obj for obj in data_from.objects if obj in objects_to_append]

        D = bpy.data
        C = bpy.context

        coll_name = 'Workspace'
        coll = C.scene.collection.children.get(coll_name)
        if coll is None:
            coll = D.collections.new(coll_name)
            coll.color_tag = 'COLOR_05'
            C.scene.collection.children.link(coll)

        for obj in data_to.objects:
            coll.objects.link(obj)

        return {'FINISHED'}

class SceneLoader(bpy.types.Operator):
    bl_idname = 'object.scene_loader'
    bl_label = 'Load Scene'

    def execute(self, context):
        import os
        path = os.path.dirname(os.path.abspath(__file__)) + r'\base.blend'

        to_append = ['Artisan']
        with bpy.data.libraries.load(path) as (data_from, data_to):
            data_to.scenes = [scene for scene in data_from.scenes if scene in to_append]

        return {'FINISHED'}

class RenderSettingsLoader(bpy.types.Operator):
    bl_idname = 'object.render_settings_loader'
    bl_label = 'Load Render Settings'

    def execute(self, context):
        print('Render Settings loaded')

        return {'FINISHED'}

class ResetAll(bpy.types.Operator):
    bl_idname = 'object.reset_all'
    bl_label = 'Reset Default'

    def execute(self, context):
        print('All resets')

        return {'FINISHED'}


# - - - - - - - - - - - - - - - - - - - - - - - -
# Register
# - - - - - - - - - - - - - - - - - - - - - - - -
cls = (
    UI_setup_panel, 
    Setup_load_panel, 
    Setup_utils_panel, 
    FigureLoader, 
    SceneLoader, 
    RenderSettingsLoader, 
    ResetAll,
) 