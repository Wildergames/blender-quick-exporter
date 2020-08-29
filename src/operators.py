import bpy
import os

class QUICKEXPORTER_OT_export_all(bpy.types.Operator):
	bl_idname = "quick_exporter.export_all"
	bl_label = "Export All"
	
	def execute(self, context):
		package_count = len(context.scene.quick_exporter.packages)

		print()
		print("Quick Exporter: Exporting All Packages (" + str(package_count) + ")")
		
		for i in range(package_count):
			bpy.ops.quick_exporter.export_single(index = i)

		return {'FINISHED'}

class QUICKEXPORTER_OT_export_single(bpy.types.Operator):
	bl_idname = "quick_exporter.export_single"
	bl_label = "Export Single"
	
	index: bpy.props.IntProperty(name="Index", default=0)

	def execute(self, context):
		package = context.scene.quick_exporter.packages[self.index]
		settings = package.settings
		
		print()
		print("Quick Exporter: Exporting Package " + str(self.index) + " (" + package.name + ")")

		# export to blend file location
		basedir = os.path.dirname(bpy.data.filepath)
		if not basedir:
			raise Exception("Quick Exporter: .blend file has not been saved. Save before exporting.")

		# Store previous selection
		prev_selection = context.selected_objects
		prev_active = context.active_object

		# Deselect all objects
		bpy.ops.object.select_all(action='DESELECT')

		for obj in package.objects:
			print("Quick Exporter:    + " + obj.pointer.name)
			obj.pointer.select_set(True)


		path = bpy.path.ensure_ext(bpy.path.abspath(package.path), '.fbx')
		print(path)
		
		bpy.ops.export_scene.fbx(
			filepath = path,
			check_existing = False,

			# Include
			use_selection = True,
			use_active_collection = False,
			object_types = { "EMPTY", "CAMERA", "LIGHT", "ARMATURE", "MESH", "OTHER" },

			# Include
			use_custom_props = settings.include.custom_properties,

			# Transform
			global_scale = settings.transform.scale,
			apply_scale_options = settings.transform.apply_scalings,
			axis_forward = settings.transform.axis_forward,
			axis_up = settings.transform.axis_up,
			apply_unit_scale = settings.transform.apply_unit,
			bake_space_transform = settings.transform.apply_transform,

			# Geometry
			mesh_smooth_type = settings.geometry.smoothing,
			use_subsurf = settings.geometry.export_subdivision_surface,
			use_mesh_modifiers  = settings.geometry.apply_modifiers,
			use_mesh_edges = settings.geometry.loose_edges,
			use_tspace  = settings.geometry.tangent_space,

			# Armature
			primary_bone_axis = settings.armature.primary_bone_axis,
			secondary_bone_axis  = settings.armature.secondary_bone_axis,
			armature_nodetype = settings.armature.armature_fbx_node_type,
			use_armature_deform_only = settings.armature.only_deform_bones,
			add_leaf_bones = settings.armature.add_leaf_bones,

			# Bake Animations
			bake_anim = settings.animation.bake,
			bake_anim_use_all_bones = settings.animation.key_all_bones,
			bake_anim_use_nla_strips = settings.animation.nla_strips,
			bake_anim_use_all_actions = settings.animation.all_actions,
			bake_anim_force_startend_keying = settings.animation.force_keying,
			bake_anim_step = settings.animation.sampling_rate,
			bake_anim_simplify_factor = settings.animation.simplify,
		)

		# Restore previous selection
		bpy.ops.object.select_all(action='DESELECT')
		context.view_layer.objects.active = prev_active
		for obj in prev_selection:
			obj.select_set(True)

		print("Quick Exporter: Exported to " + path)
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
		object_list = context.scene.quick_exporter.packages[context.scene.quick_exporter.package_index].objects
		object_list.add()
		return{'FINISHED'}

class QUICKEXPORTER_OT_package_object_list_add_selected(bpy.types.Operator):
	"""Add all selected objects to the object list."""
	bl_idname = "quick_exporter.package_object_list_add_selected"
	bl_label = "Add a new object pointer"
	
	def execute(self, context):
		print()
		print("Quick Exporter: Adding all selected objects (+ added, x skipped)")

		object_list = context.scene.quick_exporter.packages[context.scene.quick_exporter.package_index].objects

		for o in context.selected_objects:

			skip = False
			for oo in object_list:
				if oo.pointer == o:
					print("Quick Exporter:   x " + o.name)
					skip = True

			if skip:
				continue

			print("Quick Exporter:   + " + o.name)
			object_list.add()
			object_list[len(object_list) - 1].pointer = o

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