import bpy

def deselect():
    bpy.ops.object.select_all(action='DESELECT')


def unhide(obj):
    deselect()
    bpy.context.view_layer.objects.active = obj
    bpy.context.object.hide_set(False)

def select_activate(obj):
    deselect()
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

def delete_obj(obj):
    deselect()
    select_activate(obj)
    bpy.ops.object.delete(use_global=False, confirm=False)

def origin_to_geometry(obj):
    select_activate(obj)
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

def copy_object(obj, name):
    deselect()
    select_activate(obj)
    bpy.ops.object.duplicate_move()  
    bpy.context.object.name = name

def make_axis(obs, name):
    deselect()
    select_activate(obs[0])
    ctx = bpy.context.copy()
    ctx['active object'] = obs[0]
    ctx['selected_editable_objects'] = obs
    bpy.ops.object.join(ctx)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_mode(type="EDGE")
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.edge_face_add()
    bpy.ops.object.editmode_toggle()
    bpy.context.object.name = name


def save_orientation_InEditMode(obj, myType):
    deselect()
    select_activate(obj)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_mode(type=myType)
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.transform.create_orientation(use=True)
    bpy.ops.object.editmode_toggle()

