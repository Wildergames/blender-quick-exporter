import bpy

class QUICKEXPORTER_PT_panel(bpy.types.Panel):
	bl_idname = "QUICKEXPORTER_PT_panel"
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
			export_text = "Export '" + scene.quick_exporter.packages[scene.quick_exporter.package_index].name + "'"
			row.operator("quick_exporter.export_single",text=export_text).index = scene.quick_exporter.package_index
		
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
			"package_index"
		)

		column = row.column()
		column.operator("quick_exporter.add_item", text="", icon="ADD")
		column.operator("quick_exporter.remove_item", text="", icon="REMOVE")
		column.operator("quick_exporter.move_item", text="", icon="TRIA_UP").direction = 'UP'
		column.operator("quick_exporter.move_item", text="", icon="TRIA_DOWN").direction = 'DOWN'

		""" Package Editor"""
		if scene.quick_exporter.package_index >= 0 and scene.quick_exporter.packages:
			i = scene.quick_exporter.package_index
			package = scene.quick_exporter.packages[i]
			
			package_column = layout.column()
			package_column.prop(package, "name")
			package_column.prop(package, "path")

			""" Package Objects List """
			objects_box_row = package_column.row()
			objects_box_split = objects_box_row.split(factor=0.24)

			object_name_column = objects_box_split.column()
			object_name_column.label(text="Objects:")
			
			objects_box_column = objects_box_split.column()
			objects_box = objects_box_column.box()
			
			objects_add_row = objects_box.row(align=True)
			objects_add_row.operator("quick_exporter.package_object_list_add", text="Add New")
			objects_add_row.operator("quick_exporter.package_object_list_add_selected", text="Add Selected")

			objects_column_row = objects_box.row()
			objects_column = objects_column_row.column()

			if len(package.objects) <= 0:
				objects_column.label(text="No Objects Set")

			for object_index in range(len(package.objects)):
				object_row = objects_column.row()
				object_row.prop(package.objects[object_index], "pointer", text="")
				object_row.operator("quick_exporter.package_object_list_remove", text="", icon="REMOVE").index = object_index
			
			""" FBX Settings """
			fbx_settings_box = package_column.box()
			fbx_settings_box.label(text="Export Settings")
			fbx_settings_split = fbx_settings_box.split(factor=0.02)
			fbx_settings_margin_left = fbx_settings_split.column()

			fbx_settings_column = fbx_settings_split.column()

			fbx_settings_column.prop(package.settings.include, "custom_properties", text="Include Custom Properties")

			fbx_settings_column.label()
			fbx_settings_column.label(text="Transform")
			transform_box = fbx_settings_column.box()
			transform_box.prop(package.settings.transform, "scale")
			transform_box.prop(package.settings.transform, "apply_scalings")
			transform_box.prop(package.settings.transform, "axis_forward")
			transform_box.prop(package.settings.transform, "axis_up")
			transform_box.prop(package.settings.transform, "apply_unit")
			transform_box.prop(package.settings.transform, "apply_transform")


			fbx_settings_column.label()
			fbx_settings_column.label(text="Geometry")
			geo_box = fbx_settings_column.box()
			#   Smoothing
			#   Export Subdivision Surface
			geo_box.prop(package.settings.geometry, "apply_modifiers")
			#   Loose Edges
			#   Tangent Space


			fbx_settings_column.label()
			fbx_settings_column.label(text="Armature")
			armature_box = fbx_settings_column.box()
			#   Primary Bone Axis
			#   Secondary Bone Axis
			#   Only Deform Bones
			armature_box.prop(package.settings.armature, "add_leaf_bones")

			fbx_settings_column.label()
			fbx_settings_column.label(text="Animations")
			anim_box = fbx_settings_column.box()
			anim_box.prop(package.settings.animation, "bake")
			anim_box_container = anim_box.column()
			anim_box_container.enabled = package.settings.animation.bake
			anim_box_container.prop(package.settings.animation, "key_all_bones")
			anim_box_container.prop(package.settings.animation, "nla_strips")
			anim_box_container.prop(package.settings.animation, "all_actions")
			anim_box_container.prop(package.settings.animation, "force_keying")
			anim_box_container.prop(package.settings.animation, "sampling_rate")
			anim_box_container.prop(package.settings.animation, "simplify")


""" Packages List """
class QUICKEXPORTER_UL_packages_list(bpy.types.UIList):
	def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
		layout.label(text=item.name, icon = "PACKAGE")

""" Package Object List """
class QUICKEXPORTER_UL_package_object_list(bpy.types.UIList):
	def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
		layout.label(text=item.name, icon = "PACKAGE")


""" REGISTRATION """
def register():
	bpy.utils.register_class(QUICKEXPORTER_PT_panel)
	
	bpy.utils.register_class(QUICKEXPORTER_UL_packages_list)
	bpy.utils.register_class(QUICKEXPORTER_UL_package_object_list)

def unregister():
	bpy.utils.unregister_class(QUICKEXPORTER_PT_panel)
	
	bpy.utils.unregister_class(QUICKEXPORTER_UL_packages_list)
	bpy.utils.unregister_class(QUICKEXPORTER_UL_package_object_list)