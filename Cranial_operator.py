import bpy
from .Cranial_helper_functions import select_activate, unhide, delete_obj, origin_to_geometry, copy_object, make_axis, save_orientation_InEditMode

class Cranial_OT_CranialCenter(bpy.types.Operator):
    """ """
    bl_label = "Cranial reference center"
    bl_idname = "object.cranialcenter"
    
    def execute(self, context):
        try:
            unhide(bpy.data.objects["Cranial Center"])
            delete_obj(bpy.data.objects["Cranial Center"])
        except:
            pass

        bpy.ops.mesh.primitive_vert_add()
        bpy.ops.object.editmode_toggle()
        bpy.context.object.name = "Cranial Center"
       
        return {'FINISHED'}
        
        
class Cranial_OT_cylinders(bpy.types.Operator):
    """ """
    bl_label = "Normal cylinders"
    bl_idname = "object.renameshrinkwrapobj"
    bl_options = {"REGISTER", "UNDO"}
    
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        ob = bpy.context.selected_objects
        ob[0].name = "Perp_cyl"
        
        select_activate(bpy.data.objects["Perp_cyl"])
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.separate(type = 'LOOSE')
        bpy.ops.object.editmode_toggle()
        
        namelist = []
        ob = bpy.context.selected_objects
        for obj in ob:
            namelist.append(obj.name)
            
        for obj in namelist:
            
            origin_to_geometry(bpy.data.objects[obj])
            bpy.ops.view3d.snap_cursor_to_selected()
            
            bpy.ops.mesh.primitive_cylinder_add(radius=mytool.my_float_rad, depth=mytool.my_float_length, enter_editmode=False, align='WORLD')
            bpy.context.object.name = "TEMP"
            
            copy_object(bpy.data.objects['Cranial Center'], 'Cranial Center copy')
            
            make_axis([bpy.data.objects[obj], bpy.data.objects['Cranial Center copy']], "Temp axis")
            
            save_orientation_InEditMode(bpy.data.objects["Temp axis"], 'EDGE')
            
            
            select_activate(bpy.data.objects['TEMP'])
            bpy.ops.transform.transform(mode="ALIGN")
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X', constraint_axis=(True, False, False))
            bpy.context.object.name = "finalcyl"

            # bpy.ops.object.select_all(action='DESELECT')
            # bpy.data.objects['TEMP'].select_set(True)
            # bpy.context.view_layer.objects.active = bpy.data.objects['TEMP']
            # ob = bpy.context.selected_objects
            # ob[0].name = "finalcyl"
            delete_obj(bpy.data.objects[obj])
            
            
            
        for obj in bpy.context.scene.objects:
            if obj.name.startswith("finalcyl"):
                obj.select_set(True)
                
        ob = bpy.context.selected_objects
        join = []
        for obj in ob:
            join.append(obj)
        ctx = bpy.context.copy()
        ctx['active_object'] = join[0]
        ctx['selected_editable_objects'] = join
        bpy.ops.object.join(ctx)
        
            
        return {'FINISHED'}