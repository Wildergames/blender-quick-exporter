import bpy
from bpy.props import *

class QUICKEXPORTER_ObjectPointer(bpy.types.PropertyGroup):
	pointer: bpy.props.PointerProperty(
		name="Object",
		type=bpy.types.Object
	)

class QUICKEXPORTER_ExportPackageSettingsInclude(bpy.types.PropertyGroup):
	custom_properties: BoolProperty(
		name = "Custom Properties",
		description = "Export Custom Properties",
		default = True
	)

class QUICKEXPORTER_ExportPackageSettingsTransform(bpy.types.PropertyGroup):
	scale: FloatProperty(
		name="Scale",
		default=1.0
	)

	apply_scalings: EnumProperty(
		name = "Apply Scalings",
		description = "How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way)",
		default = "FBX_SCALE_NONE",
		items = {
			("FBX_SCALE_NONE", "All Local", "Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0.", "", 0),	
			("FBX_SCALE_UNITS", "FBX Units Scale", "Apply custom scaling to each object transformation, and units scaling to FBX scale.", "", 1),
			("FBX_SCALE_CUSTOM", "FBX Custom Scale", "info", "Apply custom scaling to FBX scale, and units scaling to each object transformation.", 2),
			("FBX_SCALE_ALL", "FBX All", "info", "Apply custom scaling and units scaling to FBX scale.", 3),
		}
	)

	axis_forward : EnumProperty(
		name = "Forward",
		default = "-Z",
		items = {
			("X", "X Forward", "", "", 0),
			("Y", "Y Forward", "", "", 1),
			("Z", "Z Forward", "", "", 2),
			("-X", "-X Forward", "", "", 3),
			("-Y", "-Y Forward", "", "", 4),
			("-Z", "-Z Forward", "", "", 5)
		}
	)

	axis_up : EnumProperty(
		name = "Up",
		default = "Y",
		items = {
			("X", "X Up", "", "", 0),
			("Y", "Y Up", "", "", 1),
			("Z", "Z Up", "", "", 2),
			("-X", "-X Up", "", "", 3),
			("-Y", "-Y Up", "", "", 4),
			("-Z", "-Z Up", "", "", 5)
		}
	)

	apply_unit: BoolProperty(
		name = "Apply Unit",
		description = "Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)",
		default = True
	)

	apply_transform: BoolProperty(
		name = "Apply Transform (Experimental!)",
		description = "Freeze all transforms on export. (EXPERIMENTAL!)",
		default = False
	)

class QUICKEXPORTER_ExportPackageSettingsGeometry(bpy.types.PropertyGroup):
	apply_modifiers: BoolProperty(
		name="Apply Modifiers",
		description="Applies all modifiers on export",
		default=True
	)

class QUICKEXPORTER_ExportPackageSettingsArmature(bpy.types.PropertyGroup):
	add_leaf_bones: BoolProperty(
		name="Add Leaf Bones",
		description="Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)",
		default=True
	)

class QUICKEXPORTER_ExportPackageSettingsAnimation(bpy.types.PropertyGroup):
	bake: BoolProperty(
		name="Bake",
		description="",
		default=True
	)

	key_all_bones: BoolProperty(
		name="Key All Bones",
		description="Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)",
		default=True
	)

	nla_strips: BoolProperty(
		name="NLA Strips",
		description="Export each non-muted NLA strip as a separated FBX’s AnimStack, if any, instead of global scene animation",
		default=True
	)

	all_actions: BoolProperty(
		name="All Actions",
		description="Export each action as a separated FBX’s AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)",
		default=True
	)

	force_keying: BoolProperty(
		name="Force Start/End Keying",
		description="Always add a keyframe at start and end of actions for animated channels",
		default=True
	)

	sampling_rate: FloatProperty(
		name="Sampling Rate",
		description="Sampling Rate, How often to evaluate animated values (in frames)",
		default=1
	)
	
	simplify: FloatProperty(
		name="Simplify",
		description="How much to simplify baked values (0.0 to disable, the higher the more simplified)",
		default=1
	)


			#   Key All Bones
			#   NLA Strips
			#   All Actions
			#   Force Start/End Keying
			#   Sampling Rate 
			#   Simplify


""" Package Export Settings """
class QUICKEXPORTER_ExportPackageSettings(bpy.types.PropertyGroup):
	include: PointerProperty(
		name="Include",
		type=QUICKEXPORTER_ExportPackageSettingsInclude
	)
	
	transform: PointerProperty(
		name="Transform",
		type=QUICKEXPORTER_ExportPackageSettingsTransform
	)

	geometry: PointerProperty(
		name="Geometry",
		type=QUICKEXPORTER_ExportPackageSettingsGeometry
	)

	armature: PointerProperty(
		name="Armature",
		type=QUICKEXPORTER_ExportPackageSettingsArmature
	)

	animation: PointerProperty(
		name="Animation",
		type=QUICKEXPORTER_ExportPackageSettingsAnimation
	)


""" Individual Package Data """
class QUICKEXPORTER_ExportPackage(bpy.types.PropertyGroup):
	name: StringProperty(
		name="Name",
		default="Untitled Export Package"
	)

	path: StringProperty(
		name="Path",
		subtype="FILE_PATH",
		default="/"
	)

	objects: CollectionProperty(
		name="Objects",
		type=QUICKEXPORTER_ObjectPointer
	)
		
	object_index: IntProperty(
		name="Object Index",
		description="The currently selected Object in the selected package",
		default=0
	)

	settings: PointerProperty(
		name="Export Settings",
		type=QUICKEXPORTER_ExportPackageSettings
	)


""" Data Container """
class QUICKEXPORTER_Data(bpy.types.PropertyGroup):
	packages: CollectionProperty(
		name="Packages",
		type=QUICKEXPORTER_ExportPackage)

	package_index: IntProperty(
		name="List Index",
		default=0)

	auto_export: EnumProperty(
		name="Auto Export",
		description="Whether or not to automatically export all Export Packages on save",
		default="DISABLED",
		items={
				("DISABLED", "Disabled", "Do not auto-export on save", "", 0),	
				("ENABLED", "Export All On Save", "Export all export packages each time the .blend file is saved.", "", 1)
			}
		)


""" Registration """
def register():
	bpy.utils.register_class(QUICKEXPORTER_ObjectPointer)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsInclude)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsTransform)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsGeometry)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsArmature)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsAnimation)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettings)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackage)
	bpy.utils.register_class(QUICKEXPORTER_Data)

	bpy.types.Scene.quick_exporter = bpy.props.PointerProperty(type=QUICKEXPORTER_Data)

def unregister():
	bpy.utils.unregister_class(QUICKEXPORTER_Data)
	bpy.utils.unregister_class(QUICKEXPORTER_ExportPackage)
	bpy.utils.unregister_class(QUICKEXPORTER_ExportPackageSettingsInclude)
	bpy.utils.unregister_class(QUICKEXPORTER_ExportPackageSettingsTransform)
	bpy.utils.unregister_class(QUICKEXPORTER_ExportPackageSettingsGeometry)
	bpy.utils.unregister_class(QUICKEXPORTER_ExportPackageSettingsArmature)
	bpy.utils.unregister_class(QUICKEXPORTER_ExportPackageSettingsAnimation)
	bpy.utils.unregister_class(QUICKEXPORTER_ExportPackageSettings)
	bpy.utils.unregister_class(QUICKEXPORTER_ObjectPointer)