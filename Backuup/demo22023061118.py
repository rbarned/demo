import bpy
from math import radians
from bpybb.utils import clean_scene

class Digit:
    def __init__(self, name): #, location = (0, 0, 0), rotation = (0, 0, 0)):
        self.name     = name
        self.debug = False

        bpy.ops.mesh.primitive_gear(align='WORLD', location=(0, 0, 0),     rotation=(0, 0, 0), change=False, number_of_teeth=10)
        self.gearM = bpy.context.active_object
        self.gearM.name = 'Gear_middle'
        bpy.ops.mesh.primitive_gear(align='WORLD', location=(2.1, 0, 0),     rotation=(0, 0, 0),            change=False, number_of_teeth=10)
        self.gearR = bpy.context.active_object
        self.gearR.name = 'Gear_right'
        bpy.ops.mesh.primitive_gear(align='WORLD', location=(-2.1, 0, -.25), rotation=(0, 0, 0),            change=False, number_of_teeth=10)
        self.gearL = bpy.context.active_object
        self.gearL.dimensions[2]=.9
        self.gearL.name = 'Gear_left'
        bpy.ops.mesh.primitive_gear(align='WORLD', location=(3.7, 0, -.45),   rotation=(0, 0, 0), change=False, number_of_teeth=5)
        self.gearC = bpy.context.active_object
        self.gearC.dimensions = (1.1, 1.1, .4)
        self.gearC.name = 'Gear_carry'
        self.gearMOffset = 18  # 18 degrees
        self.gearCOffset = 36  # 36 degrees
        self.addDelay = 40
        self.pauseDelay = 10

        bpy.ops.mesh.primitive_cylinder_add(vertices=10, radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, .4), scale=(.8, .8, .6)) #, rotation=(0, 0, 0)) #radians(0)))
        bpy.ops.object.convert(target='MESH')

        bpy.ops.object.editmode_toggle()

        self.cylinder = bpy.context.active_object
        bpy.ops.object.editmode_toggle()
        for i in range(10):
            self.makeTooth(i)
        bpy.ops.object.select_pattern(pattern="Cylinder")
        self.cylinder.location.x=-2.1

        bpy.ops.mesh.primitive_cylinder_add(vertices=10, radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, .4), scale=(.8, .8, .6)) #, rotation=(0, 0, 0)) #radians(0)))
        bpy.ops.object.convert(target='MESH')
        # bpy.ops.object.editmode_toggle()
        self.cylinder2 = bpy.context.active_object
        for j in range(10):
            print(j)
            self.makeTooth2(j)
        bpy.ops.object.select_pattern(pattern="Cylinder.001")
        self.cylinder2.location.x=2.1

    def makeTooth(self, nbr):
        if(True):  #nbr=="1"):
            self.cylinder.rotation_euler[2] = radians(-nbr*36)
            bpy.context.active_object.select_set(state=False)
            bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(.27,-.8,.54), scale=(.8,.8,.8), rotation=(radians(90),0,radians(18)))
            self.text1=bpy.context.active_object
            self.text1.scale = (.8,.8,.8)
            # self.text1.parent()
            # bpy.ops.object.select_pattern(pattern="Text.001")
            bpy.context.active_object.select_set(state=True)
            bpy.ops.font.delete(type='PREVIOUS_WORD')
            bpy.ops.font.text_insert(text= str(nbr))
            bpy.ops.object.editmode_toggle()
            bpy.context.object.data.align_x='CENTER'
            bpy.context.object.data.align_y='CENTER'
            bpy.context.object.data.extrude=.1
            bpy.ops.object.convert(target='MESH')
            print("Parent = " + str(self.text1.parent))
            print("self.text1 name = " +  str(self.text1.show_name))
            print(str(bpy.context.window.scene.objects[4]))
            print(str(bpy.context.window.scene.objects[5]))
            print(str(bpy.context.window.scene.objects[-1]))
            bpy.context.view_layer.objects.active = self.cylinder
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
        
    def makeTooth2(self, nbr):
        if(True):  #nbr=="1"):
            self.cylinder2.rotation_euler[2] = radians(-nbr*36)
            bpy.context.active_object.select_set(state=False)
            bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(.27,-.8,.54), scale=(.8,.8,.8), rotation=(radians(90),0,radians(18)))
            self.text2=bpy.context.active_object
            self.text2.scale = (.8,.8,.8)
            # self.text1.parent()
            # bpy.ops.object.select_pattern(pattern="Text.001")
            bpy.context.active_object.select_set(state=True)
            bpy.ops.font.delete(type='PREVIOUS_WORD')
            bpy.ops.font.text_insert(text= str(nbr))
            bpy.ops.object.editmode_toggle()
            bpy.context.object.data.align_x='CENTER'
            bpy.context.object.data.align_y='CENTER'
            bpy.context.object.data.extrude=.1
            bpy.ops.object.convert(target='MESH')
            print("Parent = " + str(self.text2.parent))
            print("self.text2 name = " +  str(self.text2.show_name))
            bpy.context.view_layer.objects.active = self.cylinder2
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)


    def printAttributes(self):
        print("debug ="+str(self.debug))

    def setadd(self, initialValue, initialResult):
        print('initialValue =', initialValue)
        print('initialResult =', initialResult)
        
        self.currentFrame = 0
        self.gearL.rotation_euler[2] = radians(-initialValue*36)
        self.gearL.keyframe_insert("rotation_euler", frame=self.currentFrame)
        self.gearM.rotation_euler[2] = radians(-18)  #radians(self.gearMOffset)
        self.gearM.keyframe_insert("rotation_euler", frame=self.currentFrame)
        # self.cylinder.rotation_euler[2] = radians(-18)  #radians(self.gearMOffset)
        self.cylinder.rotation_euler[2] = radians(-initialValue*36)+radians(-18)
        self.cylinder.keyframe_insert("rotation_euler", frame=self.currentFrame)

        self.currentFrame += self.addDelay
        self.gearL.rotation_euler[2] = radians(0*36)
        self.gearL.keyframe_insert("rotation_euler", frame=self.currentFrame)
        self.gearM.rotation_euler[2] = -radians(initialValue*36)+radians(-18)
        self.gearM.keyframe_insert("rotation_euler", frame=self.currentFrame)
        # self.cylinder.rotation_euler[2] = -radians(initialValue*36)+radians(-18)
        self.cylinder.rotation_euler[2] = radians(-18)  #radians(self.gearMOffset)
        self.cylinder.keyframe_insert("rotation_euler", frame=self.currentFrame)
        return True

clean_scene()
print('This is Robert')
digit1 = Digit('FirstDigit') 
digit1.printAttributes()
print (digit1.name)
digit1.setadd(5,0)


print('I am Robert')

