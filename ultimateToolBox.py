bl_info = {
    "name": "Ultimate Tool Box",
    "category": "Object",
}

import bpy
from bpy.types import(
        Panel,
        Operator,
        )
#Constants
GPU_TILE_SIZE = 256
CPU_TILE_SIZE = 16

HIDE_MACRO = "H_"

# OPERATORS
'''
Switch between CPU or GPU for cycles computation.
Set the approriate tile size for each mode.
'''
class OpGPU(Operator):
    bl_idname = "op.gpu"
    bl_name = "gpu"
    bl_label = "gpu"
    def execute(self, context):
        bpy.data.scenes["Scene"].cycles.device = "GPU"
        bpy.data.scenes["Scene"].render.tile_x = GPU_TILE_SIZE
        bpy.data.scenes["Scene"].render.tile_y = GPU_TILE_SIZE
        return {"FINISHED"}

class OpCPU(Operator):
    bl_idname = "op.cpu"
    bl_name = "cpu"
    bl_label = "cpu"
    def execute(self, context):
        bpy.data.scenes["Scene"].cycles.device = "CPU"
        bpy.data.scenes["Scene"].render.tile_x = CPU_TILE_SIZE
        bpy.data.scenes["Scene"].render.tile_y = CPU_TILE_SIZE
        return {"FINISHED"}


#Hide from the view and for the render every objects starting with H_
class OpHide(Operator):
    bl_idname = "op.hide"
    bl_name = "hide"
    bl_label = "hide"
    def execute(self, context):
        setProperties(True)
        return {"FINISHED"}


#Show from the view and for the render every objects starting with H_
class OpShow(Operator):
    bl_idname = "op.show"
    bl_name = "show"
    bl_label = "show"
    def execute(self, context):
        setProperties(False)
        return {"FINISHED"}

def setProperties(hideBool):
    for obj in bpy.context.scene.objects:
        if obj.name[:len(HIDE_MACRO)] == HIDE_MACRO:
            #set properties
            obj.hide_render = hideBool
            obj.hide = hideBool
            obj.hide_select = hideBool
# PANEL
class UltimateToolBoxPanel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_label = "Ultimate Toolbox"
    bl_context = "objectmode"
    bl_category = "UTB"

    def draw(self, context):
        layout = self.layout
        # GPU / CPU
        row = layout.row()
        row.label(text="Choose GPU or CPU")
        row = layout.row()
        row.operator("op.gpu", text="GPU")

        row2 = layout.row()
        row2.operator("op.cpu", text="CPU")

        # Hide objects
        rowHide = layout.row()
        rowHide.label(text="Hide / Show objects")
        rowHide = layout.row()
        rowHide.operator("op.hide", text="Hide")

        # Show objects
        rowShow = layout.row()
        rowShow.operator("op.show", text="Show")

def register():
    # Operators
    bpy.utils.register_class(OpGPU)
    bpy.utils.register_class(OpCPU)
    bpy.utils.register_class(OpHide)
    bpy.utils.register_class(OpShow)

    bpy.utils.register_class(UltimateToolBoxPanel)

def unregister():
    # Operators
    bpy.utils.unregister_class(OpGPU)
    bpy.utils.register_class(OpCPU)
    bpy.utils.register_class(OpHide)
    bpy.utils.register_class(OpShow)

    bpy.utils.unregister_class(UltimateToolBoxPanel)

if __name__ == "__main__":
    register()
