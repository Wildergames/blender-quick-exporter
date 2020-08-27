import bpy

class UNITYFBXEXPORTER_OT_export_all(bpy.types.Operator):
    bl_idname = "unity_fbx_exporter.export_all"
    bl_label = "Export All"
    
    def execute(self, context):
        print("Exporting All FBX Files")
        return {'FINISHED'}

class UNITYFBXEXPORTER_OT_export_single(bpy.types.Operator):
    bl_idname = "unity_fbx_exporter.export_single"
    bl_label = "Export Single"
    
    index: bpy.props.IntProperty(name="Index", default=0)

    def execute(self, context):
        print("Exporting Single FBX File (" + index + ")")
        return {'FINISHED'}



""" Packages List """
class UNITYFBXEXPORTER_OT_list_add(bpy.types.Operator):
    """Add a new item to the list."""
    bl_idname = "unity_fbx_exporter.add_item"
    bl_label = "Add a new item"
    
    def execute(self, context):
        context.scene.unity_fbx_exporter.packages.add()
        return{'FINISHED'}
        
class UNITYFBXEXPORTER_OT_list_remove(bpy.types.Operator):
    """Delete the selected item from the list."""
    bl_idname = "unity_fbx_exporter.remove_item"
    bl_label = "Removes an item"
    
    @classmethod
    def poll(cls, context):
        return context.scene.unity_fbx_exporter.packages
        
    def execute(self, context):
        package_list = context.scene.unity_fbx_exporter.packages
        index = context.scene.unity_fbx_exporter.package_index

        package_list.remove(index)
        context.scene.unity_fbx_exporter.package_index = min(max(0, index - 1), len(package_list) - 1)
        return{'FINISHED'}
        
class UNITYFBXEXPORTER_OT_list_move(bpy.types.Operator):
    """Move an item in the list."""
    bl_idname = "unity_fbx_exporter.move_item"
    bl_label = "Move an item in the list"
    direction: bpy.props.EnumProperty(items=(('UP', 'Up', ""), ('DOWN', 'Down', ""),))
    
    @classmethod
    def poll(cls, context):
        return context.scene.unity_fbx_exporter.packages
        
    def move_index(self):
        """ Move index of an item render queue while clamping it. """
        index = bpy.context.scene.unity_fbx_exporter.package_index
        list_length = len(bpy.context.scene.unity_fbx_exporter.packages) - 1
        new_index = index + (-1 if self.direction == 'UP' else 1)
        
        bpy.context.scene.unity_fbx_exporter.package_index = max(0, min(new_index, list_length))
        
        def execute(self, context):
            package_list = context.scene.unity_fbx_exporter.packages
            index = context.scene.unity_fbx_exporter.package_index
            neighbor = index + (-1 if self.direction == 'UP' else 1)
            package_list.move(neighbor, index)
            self.move_index()
            return{'FINISHED'}


""" Package Objects List """
class UNITYFBXEXPORTER_OT_package_object_list_add(bpy.types.Operator):
    """Add a new item to the list."""
    bl_idname = "unity_fbx_exporter.package_object_list_add"
    bl_label = "Add a new object pointer"
    
    def execute(self, context):
        context.scene.unity_fbx_exporter.packages[context.scene.unity_fbx_exporter.package_index].objects.add()
        return{'FINISHED'}
        
class UNITYFBXEXPORTER_OT_package_object_list_remove(bpy.types.Operator):
    """Delete the selected item from the list."""
    bl_idname = "unity_fbx_exporter.package_object_list_remove"
    bl_label = "Removes an object pointer"
    
    @classmethod
    def poll(cls, context):
        return context.scene.unity_fbx_exporter.packages
        
    def execute(self, context):
        object_list = context.scene.unity_fbx_exporter.packages[context.scene.unity_fbx_exporter.package_index].objects
        index = context.scene.unity_fbx_exporter.packages[context.scene.unity_fbx_exporter.package_index].object_index
        object_list.remove(index)
        context.scene.unity_fbx_exporter.packages[context.scene.unity_fbx_exporter.package_index].object_index = min(max(0, index - 1), len(object_list) - 1)
        return{'FINISHED'}
        
class UNITYFBXEXPORTER_OT_package_object_list_move(bpy.types.Operator):
    """Move an item in the list."""
    bl_idname = "unity_fbx_exporter.package_object_list_move"
    bl_label = "Move an item in the list"
    direction: bpy.props.EnumProperty(items=(('UP', 'Up', ""), ('DOWN', 'Down', ""),))
    
    @classmethod
    def poll(cls, context):
        return context.scene.unity_fbx_exporter.packages
        
    def move_index(self):
        #""" Move index of an item render queue while clamping it. """
        #index = bpy.context.scene.unity_fbx_exporter.package_index
        #list_length = len(bpy.context.scene.unity_fbx_exporter.packages) - 1 # (index starts at 0)
        #new_index = index + (-1 if self.direction == 'UP' else 1)
        #
        #bpy.context.scene.unity_fbx_exporter.package_index = max(0, min(new_index, list_length))
        pass
        
    def execute(self, context):
        #package_list = context.scene.unity_fbx_exporter.packages
        #index = context.scene.unity_fbx_exporter.package_index
        #neighbor = index + (-1 if self.direction == 'UP' else 1)
        #package_list.move(neighbor, index)
        #self.move_index()
        return{'FINISHED'}




""" Registration """
def register():
    bpy.utils.register_class(UNITYFBXEXPORTER_OT_export_single)
    bpy.utils.register_class(UNITYFBXEXPORTER_OT_export_all)

    bpy.utils.register_class(UNITYFBXEXPORTER_OT_list_add)
    bpy.utils.register_class(UNITYFBXEXPORTER_OT_list_remove)
    bpy.utils.register_class(UNITYFBXEXPORTER_OT_list_move)
    
    bpy.utils.register_class(UNITYFBXEXPORTER_OT_package_object_list_add)
    bpy.utils.register_class(UNITYFBXEXPORTER_OT_package_object_list_remove)
    bpy.utils.register_class(UNITYFBXEXPORTER_OT_package_object_list_move)

def unregister():
    bpy.utils.unregister_class(UNITYFBXEXPORTER_OT_export_single)
    bpy.utils.unregister_class(UNITYFBXEXPORTER_OT_export_all)

    bpy.utils.unregister_class(UNITYFBXEXPORTER_OT_list_add)
    bpy.utils.unregister_class(UNITYFBXEXPORTER_OT_list_remove)
    bpy.utils.unregister_class(UNITYFBXEXPORTER_OT_list_move)

    bpy.utils.unregister_class(UNITYFBXEXPORTER_OT_package_object_list_add)
    bpy.utils.unregister_class(UNITYFBXEXPORTER_OT_package_object_list_remove)
    bpy.utils.unregister_class(UNITYFBXEXPORTER_OT_package_object_list_move)