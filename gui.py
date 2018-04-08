import bpy
import math

from bpy.types import Menu

class SCREEN_pie(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Screen UI Layout"
    
    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        idx=bpy.data.window_managers['WinMan'].screen_pie_index
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        if len(bpy.data.screens)>8:
            tot=math.ceil((len(bpy.data.screens)-7)/6)
            if idx==0:
                op=pie.operator("screen_pie.change", text=bpy.data.screens[0].name)
                op.name=bpy.data.screens[0].name
                pie.operator("screen_pie.next_caller", text='', icon='FORWARD')
                for n in range(1, 7):
                    op=pie.operator("screen_pie.change", text=bpy.data.screens[n].name)
                    op.name=bpy.data.screens[n].name
            else:
                if idx!=tot:
                    min=6*idx
                    max=min+6
                    pie.operator("screen_pie.previous_caller", text='', icon='BACK')
                    pie.operator("screen_pie.next_caller", text='', icon='FORWARD')
                elif idx==tot:
                    min=7*idx
                    max=min+7
                    pie.operator("screen_pie.previous_caller", text='', icon='BACK')
                for n in range(min, max):
                    try:
                        op=pie.operator("screen_pie.change", text=bpy.data.screens[n].name)
                        op.name=bpy.data.screens[n].name
                    except IndexError:
                        pass
        else:
            for screen in bpy.data.screens:
                op=pie.operator("screen_pie.change", text=screen.name)
                op.name=screen.name
            
class SCREEN_PIE_caller(bpy.types.Operator):
    bl_idname = "screen_pie.caller"
    bl_label = "Screen UI Pie Menu"
    bl_description = ""
    bl_options = {"REGISTER"}

    

    def execute(self, context):
        bpy.data.window_managers['WinMan'].screen_pie_index=0
        bpy.ops.wm.call_menu_pie(name="SCREEN_pie")
        return {"FINISHED"}
    
class SCREEN_PIE_next_caller(bpy.types.Operator):
    bl_idname = "screen_pie.next_caller"
    bl_label = ""
    bl_description = "Go to next Screen UI Pie menu"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        idx=bpy.data.window_managers['WinMan'].screen_pie_index
        tot=math.ceil((len(bpy.data.screens)-7)/6)
        return idx>=0 and idx<=tot

    def execute(self, context):
        bpy.data.window_managers['WinMan'].screen_pie_index+=1
        bpy.ops.wm.call_menu_pie(name="SCREEN_pie")
        return {"FINISHED"}
    
class SCREEN_PIE_previous_caller(bpy.types.Operator):
    bl_idname = "screen_pie.previous_caller"
    bl_label = ""
    bl_description = "Go to previous Screen UI Pie menu"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        idx=bpy.data.window_managers['WinMan'].screen_pie_index
        return idx>0 

    def execute(self, context):
        bpy.data.window_managers['WinMan'].screen_pie_index-=1
        bpy.ops.wm.call_menu_pie(name="SCREEN_pie")
        return {"FINISHED"}