import bpy


class Screen_Pie_Change(bpy.types.Operator):
    bl_idname = "screen_pie.change"
    bl_label = ""
    bl_description = "Change UI Screen Layout to selected"
    bl_options = {"REGISTER"}
    
    name = bpy.props.StringProperty()
    
    def execute(self, context):
        bpy.context.window.screen = bpy.data.screens[self.name]
        return {"FINISHED"}
        