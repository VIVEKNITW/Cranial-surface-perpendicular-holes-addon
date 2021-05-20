import bpy

class Perpendicular_Holes(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Perpendicular Holes"
    bl_idname = "cranialplate_PT_perpendiculatholes"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "CranialPlate"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        row = layout.row()
        row.operator("object.cranialcenter")
        row = layout.row()
        row.prop(mytool, "my_float_rad")
        row.prop(mytool, "my_float_length")
        row = layout.row()
        row.operator("object.renameshrinkwrapobj")