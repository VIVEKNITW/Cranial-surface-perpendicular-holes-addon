import bpy

class CranialMyProperties(bpy.types.PropertyGroup):
    
    my_float_rad : bpy.props.FloatProperty(name= "Raduis", soft_min= 0, soft_max= 1000, default= 1)
    my_float_length : bpy.props.FloatProperty(name= "Length", soft_min= 0, soft_max= 1000, default= 5)