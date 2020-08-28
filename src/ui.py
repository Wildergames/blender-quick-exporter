import bpy

class QUICKEXPORTER_PT_ui(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = "QUICKEXPORTER_PT_ui"
    bl_label = "Quick Exporter"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene" 

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        """ Export All Button """
        row = layout.row(align=True)
        row.scale_y = 1.5

        if scene.quick_exporter and scene.quick_exporter.package_index >= 0 and len(scene.quick_exporter.packages) > scene.quick_exporter.package_index and scene.quick_exporter.packages[scene.quick_exporter.package_index]:
            row.operator("quick_exporter.export_single", text="Export '"+scene.quick_exporter.packages[scene.quick_exporter.package_index].name+"'")
        
        row.operator("quick_exporter.export_all")

        """ Auto-Export """
        row = layout.row()
        row.prop(scene.quick_exporter, "auto_export")

        """ Packages List """
        row = layout.row()
        column = row.column()
        column.template_list(
            "QUICKEXPORTER_UL_packages_list",
            "quick_exporter_list",
            scene.quick_exporter,
            "packages",
            scene.quick_exporter,
            "package_index")

        column = row.column()
        column.operator("quick_exporter.add_item", text="", icon="ADD")
        column.operator("quick_exporter.remove_item", text="", icon="REMOVE")
        column.operator("quick_exporter.move_item", text="", icon="TRIA_UP").direction = 'UP'
        column.operator("quick_exporter.move_item", text="", icon="TRIA_DOWN").direction = 'DOWN'

        """ Package Editor"""
        if scene.quick_exporter.package_index >= 0 and scene.quick_exporter.packages:
            i = scene.quick_exporter.package_index
            item = scene.quick_exporter.packages[i]
            
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
            row.operator("quick_exporter.package_object_list_add", text="Add New")
            row.operator("quick_exporter.package_object_list_add_selected", text="Add Selected")

            row = box.row()
            column = row.column()

            if len(item.objects) <= 0:
                column.label(text="No Objects Set")

            for object_index in range(len(item.objects)):
                row = column.row()
                row.prop(item.objects[object_index], "pointer", text="")
                row.operator("quick_exporter.package_object_list_remove", text="", icon="REMOVE").index = object_index
            

""" Packages List """
class QUICKEXPORTER_UL_packages_list(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        custom_icon = 'PACKAGE'
        
        # Make sure your code supports all 3 layout types
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.label(text=item.name, icon = custom_icon)
            
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon = custom_icon)


""" Package Object List """
class QUICKEXPORTER_UL_package_object_list(bpy.types.UIList):
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
    bpy.utils.register_class(QUICKEXPORTER_PT_ui)
    
    bpy.utils.register_class(QUICKEXPORTER_UL_packages_list)
    bpy.utils.register_class(QUICKEXPORTER_UL_package_object_list)

def unregister():
    bpy.utils.unregister_class(QUICKEXPORTER_PT_ui)
    
    bpy.utils.unregister_class(QUICKEXPORTER_UL_packages_list)
    bpy.utils.unregister_class(QUICKEXPORTER_UL_package_object_list)

def reload():
    pass