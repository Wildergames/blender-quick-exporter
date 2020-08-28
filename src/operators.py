import bpy

class QUICKEXPORTER_OT_export_all(bpy.types.Operator):
	bl_idname = "quick_exporter.export_all"
	bl_label = "Export All"
	
	def execute(self, context):
		print("Quick Exporter: Exporting All FBX Files")
		return {'FINISHED'}

class QUICKEXPORTER_OT_export_single(bpy.types.Operator):
	bl_idname = "quick_exporter.export_single"
	bl_label = "Export Single"
	
	index: bpy.props.IntProperty(name="Index", default=0)

	def execute(self, context):
		print("Quick Exporter: Exporting Single FBX File (" + index + ")")
		return {'FINISHED'}



""" Packages List """
class QUICKEXPORTER_OT_list_add(bpy.types.Operator):
	"""Add a new item to the list."""
	bl_idname = "quick_exporter.add_item"
	bl_label = "Add a new item"
	
	def execute(self, context):
		context.scene.quick_exporter.packages.add()
		return{'FINISHED'}
		
class QUICKEXPORTER_OT_list_remove(bpy.types.Operator):
	"""Delete the selected item from the list."""
	bl_idname = "quick_exporter.remove_item"
	bl_label = "Removes an item"
	
	@classmethod
	def poll(cls, context):
		return context.scene.quick_exporter.packages
		
	def execute(self, context):
		package_list = context.scene.quick_exporter.packages
		index = context.scene.quick_exporter.package_index

		package_list.remove(index)
		context.scene.quick_exporter.package_index = min(max(0, index - 1), len(package_list) - 1)
		return{'FINISHED'}
		
class QUICKEXPORTER_OT_list_move(bpy.types.Operator):
	"""Move an item in the list."""
	bl_idname = "quick_exporter.move_item"
	bl_label = "Move an item in the list"
	direction: bpy.props.EnumProperty(items=(('UP', 'Up', ""), ('DOWN', 'Down', ""),))
	
	@classmethod
	def poll(cls, context):
		return context.scene.quick_exporter.packages
		
	def move_index(self):
		""" Move index of an item render queue while clamping it. """
		index = bpy.context.scene.quick_exporter.package_index
		list_length = len(bpy.context.scene.quick_exporter.packages) - 1
		new_index = index + (-1 if self.direction == 'UP' else 1)
		bpy.context.scene.quick_exporter.package_index = max(0, min(new_index, list_length))
		
	def execute(self, context):
		package_list = context.scene.quick_exporter.packages
		index = context.scene.quick_exporter.package_index
		neighbor = index + (-1 if self.direction == 'UP' else 1)
		package_list.move(neighbor, index)
		self.move_index()
		return{'FINISHED'}


""" Package Objects List """
class QUICKEXPORTER_OT_package_object_list_add(bpy.types.Operator):
	"""Add a new item to the object list."""
	bl_idname = "quick_exporter.package_object_list_add"
	bl_label = "Add a new object pointer"
	
	def execute(self, context):
		context.scene.quick_exporter.packages[context.scene.quick_exporter.package_index].objects.add()
		return{'FINISHED'}

class QUICKEXPORTER_OT_package_object_list_add_selected(bpy.types.Operator):
	"""Add all selected objects to the object list."""
	bl_idname = "quick_exporter.package_object_list_add_selected"
	bl_label = "Add a new object pointer"
	
	def execute(self, context):
		
		return{'FINISHED'}
		
class QUICKEXPORTER_OT_package_object_list_remove(bpy.types.Operator):
	"""Delete the selected item from the list."""
	bl_idname = "quick_exporter.package_object_list_remove"
	bl_label = "Removes an object pointer"

	index: bpy.props.IntProperty(
		name="Object index To Remove",
		default=0
	)
	
	@classmethod
	def poll(cls, context):
		return context.scene.quick_exporter.packages
		
	def execute(self, context):
		object_list = context.scene.quick_exporter.packages[context.scene.quick_exporter.package_index].objects
		object_list.remove(self.index)
		return{'FINISHED'}



""" Registration """
def register():
	bpy.utils.register_class(QUICKEXPORTER_OT_export_single)
	bpy.utils.register_class(QUICKEXPORTER_OT_export_all)

	bpy.utils.register_class(QUICKEXPORTER_OT_list_add)
	bpy.utils.register_class(QUICKEXPORTER_OT_list_remove)
	bpy.utils.register_class(QUICKEXPORTER_OT_list_move)
	
	bpy.utils.register_class(QUICKEXPORTER_OT_package_object_list_add)
	bpy.utils.register_class(QUICKEXPORTER_OT_package_object_list_add_selected)
	bpy.utils.register_class(QUICKEXPORTER_OT_package_object_list_remove)

def unregister():
	bpy.utils.unregister_class(QUICKEXPORTER_OT_export_single)
	bpy.utils.unregister_class(QUICKEXPORTER_OT_export_all)

	bpy.utils.unregister_class(QUICKEXPORTER_OT_list_add)
	bpy.utils.unregister_class(QUICKEXPORTER_OT_list_remove)
	bpy.utils.unregister_class(QUICKEXPORTER_OT_list_move)

	bpy.utils.unregister_class(QUICKEXPORTER_OT_package_object_list_add)
	bpy.utils.unregister_class(QUICKEXPORTER_OT_package_object_list_add_selected)
	bpy.utils.unregister_class(QUICKEXPORTER_OT_package_object_list_remove)