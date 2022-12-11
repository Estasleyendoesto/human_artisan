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
        path = os.path.dirname(os.path.abspath(__file__)) + r'\artisan.blend'
        
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

        bpy.data.libraries.remove(bpy.data.libraries.get('artisan.blend'))

        return {'FINISHED'}

class SceneLoader(bpy.types.Operator):
    bl_idname = 'object.scene_loader'
    bl_label = 'Load Scene'

    def execute(self, context):
        import os
        path = os.path.dirname(os.path.abspath(__file__)) + r'\artisan.blend'

        D = bpy.data
        C = bpy.context
        with bpy.data.libraries.load(path) as (data_from, data_to):
            data_to.collections = [c for c in data_from.collections if c != 'GENESIS 9 FIGURE']

        for c in data_to.collections:
            C.scene.collection.children.link(c)
        
        bpy.data.libraries.remove(bpy.data.libraries.get('artisan.blend'))

        return {'FINISHED'}

class RenderSettingsLoader(bpy.types.Operator):
    bl_idname = 'object.render_settings_loader'
    bl_label = 'Load Render Settings'

    def execute(self, context):
        C = bpy.context

        # Cycles
        C.scene.cycles.preview_samples        = 512
        C.scene.cycles.use_preview_denoising  = True
        C.scene.cycles.preview_denoiser       = 'OPTIX'
        C.scene.cycles.preview_denoising_input_passes = 'RGB_ALBEDO_NORMAL'
        C.scene.cycles.samples                = 720
        C.scene.cycles.use_denoising          = True
        C.scene.cycles.denoiser               = 'OPTIX'
        C.scene.cycles.denoising_input_passes = 'RGB_ALBEDO_NORMAL'
        # Cycles - Light Paths
        C.scene.cycles.max_bounces             = 6
        C.scene.cycles.diffuse_bounces         = 2
        C.scene.cycles.glossy_bounces          = 3
        C.scene.cycles.transmission_bounces    = 6
        C.scene.cycles.volume_bounces          = 1
        C.scene.cycles.transparent_max_bounces = 32
        # Color Management
        C.scene.view_settings.view_transform    = 'Filmic'
        C.scene.view_settings.look              = 'Medium Low Contrast'
        C.scene.view_settings.exposure          = 0.4
        C.scene.view_settings.gamma             = 0.8   
        C.scene.view_settings.use_curve_mapping = True

        return {'FINISHED'}

class ResetAll(bpy.types.Operator):
    bl_idname = 'object.reset_all'
    bl_label = 'Reset Default'

    def execute(self, context):
        C = bpy.context
        # Cycles
        C.scene.cycles.preview_samples        = 1024
        C.scene.cycles.use_preview_denoising  = False
        C.scene.cycles.preview_denoiser       = 'AUTO'
        C.scene.cycles.preview_denoising_input_passes = 'RGB_ALBEDO'
        C.scene.cycles.samples                = 4096
        C.scene.cycles.use_denoising          = True
        C.scene.cycles.denoiser               = 'OPENIMAGEDENOISE'
        C.scene.cycles.denoising_input_passes = 'RGB_ALBEDO_NORMAL'
        # Cycles - Light Paths
        C.scene.cycles.max_bounces             = 12
        C.scene.cycles.diffuse_bounces         = 4
        C.scene.cycles.glossy_bounces          = 4
        C.scene.cycles.transmission_bounces    = 12
        C.scene.cycles.volume_bounces          = 0
        C.scene.cycles.transparent_max_bounces = 8
        # Color Management
        C.scene.view_settings.view_transform    = 'Filmic'
        C.scene.view_settings.look              = 'None'
        C.scene.view_settings.exposure          = 0
        C.scene.view_settings.gamma             = 1
        C.scene.view_settings.use_curve_mapping = False

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