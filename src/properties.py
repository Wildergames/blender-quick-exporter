import bpy

class QUICKEXPORTER_ObjectPointer(bpy.types.PropertyGroup):
	pointer: bpy.props.PointerProperty(
		name="Object",
		type=bpy.types.Object
	)

	def update(self, context):
		print("UPDATING!"); 

""" Individual Package Data """
class QUICKEXPORTER_ExportPackage(bpy.types.PropertyGroup):
	name: bpy.props.StringProperty(
		name="Name",
		default="Untitled Export Package")

	path: bpy.props.StringProperty(
		name="Path",
		subtype="FILE_PATH",
		default="/")

	objects: bpy.props.CollectionProperty(
		name="Objects",
		type=QUICKEXPORTER_ObjectPointer)
		
	object_index: bpy.props.IntProperty(
		name="Object Index",
		description="The currently selected Object in the selected package",
		default=0)

	scale: bpy.props.FloatProperty(
		name="Scale",
		default=1)

	applyTransform: bpy.props.BoolProperty(
		name="Apply Transform",
		description="Freeze all transforms on export. (EXPERIMENTAL!)",
		default=True)
	
	applyModifiers: bpy.props.BoolProperty(
		name="Apply Modifiers",
		description="Applies all modifiers on export",
		default=True) 


""" Data Container """
class QUICKEXPORTER_Data(bpy.types.PropertyGroup):
	packages: bpy.props.CollectionProperty(
		name="Packages",
		type=QUICKEXPORTER_ExportPackage)

	package_index: bpy.props.IntProperty(
		name="List Index",
		default=0)

	auto_export: bpy.props.EnumProperty(
		name="Auto Export",
		description="Whether or not to automatically export all Export Packages on save",
		default="DISABLED",
		items={
			("DISABLED", "Disabled", 'Do not auto-export on save', '', 0),
			("ENABLED", 'Export All On Save', 'Export all export packages each time the .blend file is saved.', '', 1)
			}
		)


""" Registration """
def register():
	bpy.utils.register_class(QUICKEXPORTER_ObjectPointer)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackage)
	bpy.utils.register_class(QUICKEXPORTER_Data)

	bpy.types.Scene.quick_exporter = bpy.props.PointerProperty(type=QUICKEXPORTER_Data)

def unregister():
	bpy.utils.unregister_class(QUICKEXPORTER_ExportPackage)
	bpy.utils.unregister_class(QUICKEXPORTER_Data)
	bpy.utils.unregister_class(QUICKEXPORTER_ObjectPointer)