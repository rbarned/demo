import bpy
from math import radians
from bpybb.utils import clean_scene

class Digit:
    def __init__(self, name): #, location = (0, 0, 0), rotation = (0, 0, 0)):
        self.name     = name
        self.debug = False
        # self.location = location
        # self.rotation = rotation
        
        
        #try the following
        #bpy.context.area.ui_type='PROPERTIES'
        #bpy.context.space_data.context='OBJECT'
        #bpy.context.space_data.context='DATA'
        #bpy.context.object.modifiers["Boolean"].operation='UNION'




        bpy.ops.mesh.primitive_gear(align='WORLD', location=(0, 0, 0),     rotation=(0, 0, 0), change=False, number_of_teeth=10)
        self.gearM = bpy.context.active_object
        self.gearM.name = 'Gear_middle'
        bpy.ops.mesh.primitive_gear(align='WORLD', location=(2.1, 0, 0),     rotation=(0, 0, 0),            change=False, number_of_teeth=10)
        self.gearR = bpy.context.active_object
        self.gearR.name = 'Gear_right'
        bpy.ops.mesh.primitive_gear(align='WORLD', location=(-2.1, 0, -.25), rotation=(0, 0, 0),            change=False, number_of_teeth=10)
        self.gearL = bpy.context.active_object
     #   bpy.ops.mesh.primitive_gear(align='WORLD', location=(0, 0, 0),       rotation=(0, 0, radians(-18)), change=False, number_of_teeth=10)
        self.gearL.dimensions[2]=.9
        self.gearL.name = 'Gear_left'
        bpy.ops.mesh.primitive_gear(align='WORLD', location=(3.7, 0, -.45),   rotation=(0, 0, 0), change=False, number_of_teeth=5)
        self.gearC = bpy.context.active_object
        self.gearC.dimensions = (1.1, 1.1, .4)
        self.gearC.name = 'Gear_carry'
        #self.gearC.hide_set(True)
        self.gearMOffset = 18  # 18 degrees
        self.gearCOffset = 36  # 36 degrees
        self.addDelay = 40
        self.pauseDelay = 10

        bpy.ops.mesh.primitive_cylinder_add(vertices=10, radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, .4), scale=(.8, .8, .6)) #, rotation=(0, 0, 0)) #radians(0)))
        bpy.ops.object.convert(target='MESH')

        bpy.ops.object.editmode_toggle()
        bpy.context.active_object.rotation_euler = (0, 0, radians(54))

        self.cylinder = bpy.context.active_object
        # self.cylinder.rotation_euler[2] = radians(54) #-18)
        bpy.ops.object.editmode_toggle()
        # bpy.ops.object.text_add(enter_editmode=True, location=(0,-.8,.58), rotation=(89.7,0,0))
        
        self.makeTooth('0')
        # bpy.ops.object.select_pattern(pattern="Cylinder")
        self.cylinder.rotation_euler[2] = radians(-54)  #-18-(36*1))
        self.makeTooth('1')

        # bpy.ops.object.text_add(enter_editmode=True, align='VIEW', location=(.27,-.8,.54), scale=(.8,.8,.8), rotation=(radians(90),0,radians(18)))
        # self.text=bpy.context.active_object
        # self.text.scale = (.8,.8,.8)
        # bpy.ops.font.delete(type='PREVIOUS_WORD')
        # bpy.ops.font.text_insert(text= '0')
        # bpy.ops.object.editmode_toggle()
        # bpy.context.object.data.align_x='CENTER'
        # bpy.context.object.data.align_y='CENTER'
        # bpy.context.object.data.extrude=.1
        # bpy.ops.object.convert(target='MESH')
        # self.text.select_set(True)
        # bpy.context.object.parent = bpy.data.objects["Cylinder"]
        
        bpy.ops.object.select_pattern(pattern="Cylinder")
        # self.cylinder.location.x=-2.1

        # bpy.ops.object.select_pattern(pattern="Gear_left")
        # self.gearL = bpy.context.active_object
        # bpy.ops.view3d.snap_selected_to_active()
        # bpy.context.object.parent = bpy.data.objects["Gear_left"]
        # bpy.data.objects['Text'].select_set(False)
         # bpy.ops.object.join()


    def makeTooth(self, nbr):
        if(nbr=="1"):
            self.cylinder.rotation_euler[2] = radians(-108)
            print('Tried to rotate cylinder')
            bpy.context.active_object.select_set(state=False)
            bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(.27,-.8,.54), scale=(.8,.8,.8), rotation=(radians(90),0,radians(18)))
            self.text1=bpy.context.active_object
            self.text1.scale = (1.2,1.2,1.2)
            # self.text1.parent()
            # bpy.ops.object.select_pattern(pattern="Text.001")
            bpy.context.active_object.select_set(state=True)
            bpy.ops.font.delete(type='PREVIOUS_WORD')
            bpy.ops.font.text_insert(text= nbr)
            bpy.ops.object.editmode_toggle()
            bpy.context.object.data.align_x='CENTER'
            bpy.context.object.data.align_y='CENTER'
            bpy.context.object.data.extrude=.1
            bpy.ops.object.convert(target='MESH')
            print("Parent = " + str(self.text1.parent))
            print("self.text1 name = " +  str(self.text1.show_name))
            # self.text1.__setattr__.__name__ = "Newn"

            # obj = bpyy.context.scene.objects["Text001"]
            # obj2 = bpyy.context.scene.objects["Text002"]
            # self.text1.ops.font.delete(type='PREVIOUS_WORD')
            # self.text1.ops.font.text_insert(text= nbr)
            # self.text1.ops.object.editmode_toggle()
            # self.text1.context.object.data.align_x='CENTER'
            # self.text1.context.object.data.align_y='CENTER'
            # self.text1.context.object.data.extrude=.1
            # self.text1.ops.object.convert(target='MESH')
            # self.text1.select_set(True)
            # bpy.context.active_object.select_set(state=False)
            # bpy.ops.object.select_pattern(pattern="Text001")
            # bpy.ops.object.select_pattern(pattern="Cylinder")
            # bpy.ops.object.select_pattern(pattern="Text001")
            # bpy.context.object.parent = bpy.data.objects["Cylinder"]
            # bpy.context.object.parent = bpy.data.objects["Text001"]
            print(str(bpy.context.window.scene.objects[0]))
            print(str(bpy.context.window.scene.objects[1]))
            print(str(bpy.context.window.scene.objects[2]))
            print(str(bpy.context.window.scene.objects[3]))
            print(str(bpy.context.window.scene.objects[4]))
            print(str(bpy.context.window.scene.objects[5]))
            print(str(bpy.context.window.scene.objects[6]))
            # print(str(bpy.context.window.scene.objects[7]))
            # print(str(bpy.context.window.scene.objects[8]))
            obj = bpy.context.window.scene.objects[4]
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
            # self.text1.__setattr__.__name__ = "Newn"
        else:
            bpy.ops.object.text_add(enter_editmode=True, align='WORLD', location=(.27,-.8,.54), scale=(.8,.8,.8), rotation=(radians(90),0,radians(18)))
            self.text=bpy.context.active_object
            self.text.scale = (.8,.8,.8)
            bpy.ops.font.delete(type='PREVIOUS_WORD')
            bpy.ops.font.text_insert(text= nbr)
            bpy.ops.object.editmode_toggle()
            bpy.context.object.data.align_x='CENTER'
            bpy.context.object.data.align_y='CENTER'
            bpy.context.object.data.extrude=.1
            bpy.ops.object.convert(target='MESH')
            self.text.select_set(True)
            bpy.context.object.parent = bpy.data.objects["Cylinder"]
        

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
digit1 = Digit('FirstDigit') #, location=(0, 0, 0), rotation=(5, 5, 6))
digit1.printAttributes()
print (digit1.name)
digit1.setadd(5,0)
# print (digit1.location)
# print (digit1.rotation)
# print (digit1.location[1])
# print (digit1.rotation[1])

# bpy.ops.mesh.primitive_gear(align='WORLD', location=(0, 0, 0),       rotation=(0, 0, radians(-18)), change=False, number_of_teeth=10)
# gearM = bpy.context.active_object
# gearM.name = 'Gear_middle'
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(2.1, 0, 0),     rotation=(0, 0, 0),            change=False, number_of_teeth=10)
# gearR = bpy.context.active_object
# gearR.name = 'Gear_right'
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(-2.1, 0, -.25), rotation=(0, 0, 0),            change=False, number_of_teeth=10)
# gearL = bpy.context.active_object
# gearL.dimensions[2]=.9
# gearL.name = 'Gear_left'
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(3.7, 0, -.45),   rotation=(0, 0, 0), change=False, number_of_teeth=5)
# gearC = bpy.context.active_object
# gearC.dimensions = (1.1, 1.1, .4)
# gearC.name = 'Gear_carry'
# gearC.hide_set(True)

# bpy.ops.mesh.primitive_gear(align='WORLD', location=(0, 0, 1.5),     rotation=(0, 0, radians(-18)), change=False, number_of_teeth=10)
# gearM1 = bpy.context.active_object
# gearM1.name = 'Gear1_middle'
# gearM1.hide_set(True)
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(2.1, 0, 1.5),   rotation=(0, 0, 0),            change=False, number_of_teeth=10)
# gearR1 = bpy.context.active_object
# gearR1.name = 'Gear1_right'
# gearR1.hide_set(True)
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(-2.1, 0, 1.25), rotation=(0, 0, 0),            change=False, number_of_teeth=10)
# gearL1 = bpy.context.active_object
# gearL1.dimensions[2]=.9
# gearL1.name = 'Gear1_left'
# gearL1.hide_set(True)
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(3.7, 0, 1.05),   rotation=(0, 0, 0), change=False, number_of_teeth=5)
# gearC1 = bpy.context.active_object
# gearC1.dimensions = (1.1, 1.1, .4)
# gearC1.name = 'Gear1_carry'
# gearC1.hide_set(True)

# bpy.ops.mesh.primitive_gear(align='WORLD', location=(0, 0, 3),       rotation=(0, 0, radians(-18)), change=False, number_of_teeth=10)
# gearM2 = bpy.context.active_object
# gearM2.name = 'Gear2_middle'
# gearM2.hide_set(True)
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(2.1, 0, 3),     rotation=(0, 0, 0),            change=False, number_of_teeth=10)
# gearR2 = bpy.context.active_object
# gearR2.name = 'Gear2_right'
# gearR2.hide_set(True)
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(-2.1, 0, 2.75), rotation=(0, 0, 0),            change=False, number_of_teeth=10)
# gearL2 = bpy.context.active_object
# gearL2.dimensions[2]=.9
# gearL2.name = 'Gear2_left'
# gearL2.hide_set(True)
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(3.7, 0, 2.55),   rotation=(0, 0, 0), change=False, number_of_teeth=5)
# gearC2 = bpy.context.active_object
# gearC2.dimensions = (1.1, 1.1, .4)
# gearC2.name = 'Gear2_carry'
# gearC2.hide_set(True)

# bpy.ops.mesh.primitive_gear(align='WORLD', location=(0, 0, 4.5),     rotation=(0, 0, radians(-18)), change=False, number_of_teeth=10)
# gearM3 = bpy.context.active_object
# gearM3.name = 'Gear3_middle'
# gearM3.hide_set(True)
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(2.1, 0, 4.5),   rotation=(0, 0, 0),            change=False, number_of_teeth=10)
# gearR3 = bpy.context.active_object
# gearR3.name = 'Gear3_right'
# gearR3.hide_set(True)
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(-2.1, 0, 4.25), rotation=(0, 0, 0),            change=False, number_of_teeth=10)
# gearL3 = bpy.context.active_object
# gearL3.dimensions[2]=.9
# gearL3.name = 'Gear3_left'
# gearL3.hide_set(True)
# bpy.ops.mesh.primitive_gear(align='WORLD', location=(3.7, 0, 4.05),   rotation=(0, 0, 0), change=False, number_of_teeth=5)
# gearC3 = bpy.context.active_object
# gearC3.dimensions = (1.1, 1.1, .4)
# gearC3.name = 'Gear3_carry'
# gearC3.hide_set(True)


# bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(9, 0, -.2), rotation=(1.5708, 0, 0), scale=(.5, .5, .5))
# text1 = bpy.context.active_object
# text1.dimensions = (1.5, .4, .4)
# text1.name = 'Text1'
# text1.data.body = 'Carry Pending'
# text1.hide_set(True)
# bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(9, 0, 1.4), rotation=(1.5708, 0, 0), scale=(.5, .5, .5))
# text2 = bpy.context.active_object
# text2.dimensions = (1.5, .4, .4)
# text2.name = 'Text2'
# text2.data.body = 'Carry Pending'
# text2.hide_set(True)
# bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(9, 0, 2.8), rotation=(1.5708, 0, 0), scale=(.5, .5, .5))
# text3 = bpy.context.active_object
# text3.dimensions = (1.5, .4, .4)
# text3.name = 'Text3'
# text3.data.body = 'Carry Pending'
# text3.hide_set(True)
# bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(9, 0, 4.2), rotation=(1.5708, 0, 0), scale=(.5, .5, .5))
# text4 = bpy.context.active_object
# text4.dimensions = (1.5, .4, .4)
# text4.name = 'Text4'
# text4.data.body = 'Carry Pending'
# text4.hide_set(True)
# #text4.hide_set(False)



# pause_interval =   30
# start_frame    =    1  # Teeth engaged, initial values set
# add1_frame     =   90  # Addition complete
# down1_frame    =  100  # Teeth disengaged
# reset1_frame   =  280  # Subtraction complete
# up2_frame      =  340  # Teeth engaged
# add2_frame     =  460  # 1st addition *2
# down2_frame    =  520 # Teeth disengaged
# reset2_frame   =  690 # Subtraction complete
# up3_frame      =  760 # Teeth engaged
# add3_frame     =  850  # Addition complete
# down3_frame    =  960  # Teeth disengaged
# reset3_frame   = 1080  # Subtraction complete
# up4_frame      = 1150  # Teeth engaged
# add4_frame     = 1220  # 1st addition *2
# down4_frame    = 1280 # Teeth disengaged
# reset4_frame   = 1450 # Subtraction complete
# up5_frame      = 1510 # Teeth engaged
# end_frame      = 1600

# gearL.rotation_euler[2] = radians(-5 * 36)  # Initial value 5
# gearM.keyframe_insert("location", frame=start_frame)

# gearL.keyframe_insert("rotation_euler", frame=start_frame)
# gearM.keyframe_insert("rotation_euler", frame=start_frame)
# gearR.keyframe_insert("rotation_euler", frame=start_frame)
# gearC.keyframe_insert("rotation_euler", frame=start_frame)
 
# gearL.rotation_euler.z = radians(0)      # value 0h
# gearL.keyframe_insert("rotation_euler", frame=add1_frame)
# gearM.rotation_euler.z = radians((-5*36)-18)  # value 5
# gearM.keyframe_insert("rotation_euler", frame=add1_frame)
# gearR.rotation_euler.z = radians(5*36)      # value 5
# gearR.keyframe_insert("rotation_euler", frame=add1_frame)1
# gearM.keyframe_insert("location",       frame=add1_frame)
# gearC.rotation_euler.z = radians(-5*72)      # value 5
# gearC.keyframe_insert("rotation_euler", frame=add1_frame)

# gearM.location[2]=-.45
# gearM.keyframe_insert("location", frame=down1_frame)

# gearL.rotation_euler.z = radians((-5*36)-18)      # value -5
# gearL.keyframe_insert("rotation_euler", frame=reset1_frame)
# gearM.rotation_euler.z = radians(0)  # value 
# gearM.keyframe_insert("rotation_euler", frame=reset1_frame)


# ################ New Code ################

# gearM_offset = -18
# gearC_offset = -36
print('I am Robert')

