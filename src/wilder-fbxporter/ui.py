import bpy

class UNITYFBXEXPORTER_PT_ui(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = "UNITYFBXEXPORTER_PT_ui"
    bl_label = "Unity FBX Exporter"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene" 

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        """ Export All Button """
        row = layout.row(align=True)
        row.scale_y = 1.5

        if scene.unity_fbx_exporter and scene.unity_fbx_exporter.package_index >= 0 and scene.unity_fbx_exporter.packages[scene.unity_fbx_exporter.package_index]:
            row.operator("unity_fbx_exporter.export_single", text="Export '"+scene.unity_fbx_exporter.packages[scene.unity_fbx_exporter.package_index].name+"'")
        
        row.operator("unity_fbx_exporter.export_all")

        """ Packages List """
        row = layout.row()
        column = row.column()
        column.template_list(
            "UNITYFBXEXPORTER_UL_packages_list",
            "unity_fbx_exporter_list",
            scene.unity_fbx_exporter,
            "packages",
            scene.unity_fbx_exporter,
            "package_index")

        column = row.column()
        column.operator("unity_fbx_exporter.add_item", text="", icon="ADD")
        column.operator("unity_fbx_exporter.remove_item", text="", icon="REMOVE")
        column.operator("unity_fbx_exporter.move_item", text="", icon="TRIA_UP").direction = 'UP'
        column.operator("unity_fbx_exporter.move_item", text="", icon="TRIA_DOWN").direction = 'DOWN'

        """ Package Editor"""
        if scene.unity_fbx_exporter.package_index >= 0 and scene.unity_fbx_exporter.packages:
            i = scene.unity_fbx_exporter.package_index
            item = scene.unity_fbx_exporter.packages[i]
            
            row = layout.row()
            column = row.column()

            box = column.box()
            column = box.column()
            column.prop(item, "name")
            column.prop(item, "path")

            """ Package Objects List """
            row = column.row()
            split = row.split(factor=0.24)

            column = split.column()
            column.label(text="Objects:")
            
            column = split.column()
            box = column.box()

            row = box.row(align=True)
            row.operator("unity_fbx_exporter.package_object_list_add", text="Add New")
            row.operator("unity_fbx_exporter.package_object_list_add", text="Add Selected")

            row = box.row()
            column = row.column()

            if len(item.objects) <= 0:
                column.label(text="No Objects Set")

            for object_index in range(len(item.objects)):
                row = column.row()
                row.prop(item.objects[object_index], "pointer", text="")
                row.operator("unity_fbx_exporter.package_object_list_remove", text="", icon="REMOVE").index = object_index
            

""" Packages List """
class UNITYFBXEXPORTER_UL_packages_list(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        custom_icon = 'PACKAGE'
        
        # Make sure your code supports all 3 layout types
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, icon = custom_icon)
            
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon = custom_icon)


""" Package Object List """
class UNITYFBXEXPORTER_UL_package_object_list(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        custom_icon = 'PACKAGE'
        
        # Make sure your code supports all 3 layout types
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, icon = custom_icon)
            
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon = custom_icon)


""" REGISTRATION """
def register():
    bpy.utils.register_class(UNITYFBXEXPORTER_PT_ui)
    
    bpy.utils.register_class(UNITYFBXEXPORTER_UL_packages_list)
    bpy.utils.register_class(UNITYFBXEXPORTER_UL_package_object_list)

def unregister():
    bpy.utils.unregister_class(UNITYFBXEXPORTER_PT_ui)
    
    bpy.utils.unregister_class(UNITYFBXEXPORTER_UL_packages_list)
    bpy.utils.unregister_class(UNITYFBXEXPORTER_UL_package_object_list)

def reload():
    pass