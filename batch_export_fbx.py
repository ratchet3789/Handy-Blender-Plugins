bl_info = {
	"name": "Ratchets Batch FBX Exporter",
	"author": "Ratchet3789",
	"version": (0,1,0),
	"description": "Batch exports FBX files to the save location of your Blend file.",
	"category": "Object",
}

import bpy

class BatchFBXExport(bpy.types.Operator):
    """Mass export to FBX""" # blender will use this as a tool-tip for menu items and buttons.
    bl_idname = "object.batch_export_fbx" # unique identifier for buttons and menu items to reference.
    bl_label = "Batch FBX Export"			# display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}	# enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.

    # The original script
        for x in bpy.context.selected_objects:
            basedir = os.path.dirname(bpy.data.filepath)
            name = bpy.path.clean_name(x.name)
            fn = os.path.join(basedir, name)
            bpy.obs.export_scene.fbx(filepath=fn + ".fbx", use_selection=True)

        return {'FINISHED'}            # this lets blender know the operator finished successfully.


def register():
    bpy.utils.register_class(BatchFBXExport)


def unregister():
    bpy.utils.unregister_class(BatchFBXExport)


# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()