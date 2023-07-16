import bpy
#import sys

#print(sys.path)

print ('this is robert')

bpy.ops.mesh.primitive_cube_add(size=4)
cube_obj = bpy.context.active_object

cube_obj.location.x = 5
cube_obj.location.y = 5
cube_obj.location.z = 5
