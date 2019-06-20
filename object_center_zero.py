import bpy
bl_info = {
    "name": "Ratchets Center All Objects",
    "author": "Ratchet3789",
    "version": (0, 1, 0),
    "description": "Centers all selected objects. Built for Game Development.",
    "category": "Object",
}


class CenterOriginToZero(bpy.types.Operator):
    """Center all objects script"""  # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.center_all_in_level"  # unique identifier for buttons and menu items to reference.
    bl_label = "Center Origin (Zero)"			# display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    # execute() is called by blender when running the operator.
    def execute(self, context):

        # The original script
        for x in bpy.context.selected_objects:
            x.location = (0, 0, 0)
        # this lets blender know the operator finished successfully.
        return {'FINISHED'}

class SnapMeshToOrigin(bpy.types.Operator):
    """ABSOLUTE Zero of all objects within the scene"""
    bl_idname = "object.snap_to_origin"
    bl_label = "Center Mesh (Zero)"
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):
        
        for x in bpy.context.selected_objects:
            x.select = True
            bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
        return {'FINISHED'}

class AbsoluteCenterObjects(bpy.types.Operator):
    """ABSOLUTE Zero of all objects within the scene"""
    bl_idname = "object.absolute_center_all_in_level"
    bl_label = "Center All (Zero)"
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):
        for x in bpy.context.selected_objects:
            x.select = True
            bpy.ops.object.origin_set(type="GEOMETRY_ORIGIN")
            x.location = (0, 0, 0)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(CenterOriginToZero)
    bpy.utils.register_class(SnapMeshToOrigin)
    bpy.utils.register_class(AbsoluteCenterObjects)

def unregister():
    bpy.utils.unregister_class(CenterOriginToZero)
    bpy.utils.unregister_class(SnapMeshToOrigin)
    bpy.utils.unregister_class(AbsoluteCenterObjects)

# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()
