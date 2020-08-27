import bpy

class UNITYFBXEXPORTER_OT_ExportAll(bpy.types.Operator):
    bl_idname = "unity_fbx_exporter.export_all"
    bl_label = "Export All"
    
    def execute(self, context):
        print("Exporting All FBX Files")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(UNITYFBXEXPORTER_OT_ExportAll)

def unregister():
    bpy.utils.unregister_class(UNITYFBXEXPORTER_OT_ExportAll)