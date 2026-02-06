'''
--------------------------------------------------------
Quick Exporter  -  Blender addon   -   by Tony Coculuzzi
https://wilder.games  -  https://twitter.com/wildergames
--------------------------------------------------------

For license information, see the READEME and/or LICENSE
files on the official GitHub repository:

https://github.com/wildergames/blender-quick-exporter

--------------------------------------------------------
'''

import bpy
from bpy.props import *

class QUICKEXPORTER_ObjectPointer(bpy.types.PropertyGroup):
	pointer: bpy.props.PointerProperty(
		name="Object",
		type=bpy.types.Object
	)

class QUICKEXPORTER_CollectionPointer(bpy.types.PropertyGroup):
	pointer: bpy.props.PointerProperty(
		name="Collection",
		type=bpy.types.Collection
	)

class QUICKEXPORTER_ExportPackageSettingsInclude(bpy.types.PropertyGroup):

	def copy_from(self, old):
		self.custom_properties = old.custom_properties

	expanded: BoolProperty(
		name = "Expanded",
		default = True
	)

	custom_properties: BoolProperty(
		name = "Custom Properties",
		description = "Export Custom Properties",
		default = True
	)

class QUICKEXPORTER_ExportPackageSettingsTransform(bpy.types.PropertyGroup):

	def copy_from(self, old):
		self.scale = old.scale
		self.apply_scalings = old.apply_scalings
		self.axis_forward = old.axis_forward
		self.axis_up = old.axis_up
		self.apply_unit = old.apply_unit
		self.apply_transform = old.apply_transform

	expanded: BoolProperty(
		name = "Expanded",
		default = True
	)

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

	def copy_from(self, old):
		self.smoothing = old.smoothing
		self.export_subdivision_surface = old.export_subdivision_surface
		self.apply_modifiers = old.apply_modifiers
		self.loose_edges = old.loose_edges
		self.tangent_space = old.tangent_space

	expanded: BoolProperty(
		name = "Expanded",
		default = True
	)

	smoothing : EnumProperty(
		name = "Smoothing",
		description = "Export smoothing information (prefer ‘Normals Only’ option if your target importer understand split normals)",
		default = "OFF",
		items = {
			("OFF", "Normals Only", "", "", 0),
			("FACE", "Face", "", "", 1),
			("EDGE", "Edge", "", "", 2),
		}
	)

	export_subdivision_surface: BoolProperty(
		name = "Export Subdivision Surface",
		description = "Export the last Catmull-Rom subdivision modifier as FBX subdivision (does not apply the modifier even if ‘Apply Modifiers’ is enabled)",
		default = False
	)

	apply_modifiers: BoolProperty(
		name = "Apply Modifiers",
		description = "Applies all modifiers on export",
		default = True
	)

	loose_edges: BoolProperty(
		name = "Loose Edges",
		description = "Export loose edges (as two-vertices polygons)",
		default = False
	)

	tangent_space: BoolProperty(
		name = "Tangent Space",
		description = "Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)",
		default = False
	)

class QUICKEXPORTER_ExportPackageSettingsArmature(bpy.types.PropertyGroup):

	def copy_from(self, old):
		self.primary_bone_axis = old.primary_bone_axis
		self.secondary_bone_axis = old.secondary_bone_axis
		self.armature_fbx_node_type = old.armature_fbx_node_type
		self.only_deform_bones = old.only_deform_bones
		self.add_leaf_bones = old.add_leaf_bones

	expanded: BoolProperty(
		name = "Expanded",
		default = True
	)

	primary_bone_axis : EnumProperty(
		name = "Primary Bone Axis",
		default = "Y",
		items = {
			("X", "X Axis", "", "", 0),
			("Y", "Y AxAxis", "", "", 1),
			("Z", "Z AxAxis", "", "", 2),
			("-X", "-X Axis", "", "", 3),
			("-Y", "-Y Axis", "", "", 4),
			("-Z", "-Z Axis", "", "", 5)
		}
	)

	secondary_bone_axis : EnumProperty(
		name = "Secondary Bone Axis",
		default = "X",
		items = {
			("X", "X Axis", "", "", 0),
			("Y", "Y AxAxis", "", "", 1),
			("Z", "Z AxAxis", "", "", 2),
			("-X", "-X Axis", "", "", 3),
			("-Y", "-Y Axis", "", "", 4),
			("-Z", "-Z Axis", "", "", 5)
		}
	)

	armature_fbx_node_type : EnumProperty(
		name = "Armature FBXNode Type",
		description = " FBX type of node (object) used to represent Blender’s armatures (use Null one unless you experience issues with other app, other choices may no import back perfectly in Blender…)",
		default = "NULL",
		items = {
			("NULL", "Null", "", "", 0),
			("ROOT", "Root", "", "", 1),
			("LIMBNODE", "Limb Node", "", "", 2),
		}
	)

	only_deform_bones: BoolProperty(
		name = "Only Deform Bones",
		description = "Only write deforming bones (and non-deforming ones when they have deforming children)",
		default = False
	)

	add_leaf_bones: BoolProperty(
		name = "Add Leaf Bones",
		description = "Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)",
		default = True
	)

class QUICKEXPORTER_ExportPackageSettingsAnimation(bpy.types.PropertyGroup):

	def copy_from(self, old):
		self.bake = old.bake
		self.key_all_bones = old.key_all_bones
		self.nla_strips = old.nla_strips
		self.all_actions = old.all_actions
		self.force_keying = old.force_keying
		self.sampling_rate = old.sampling_rate
		self.simplify = old.simplify

	expanded: BoolProperty(
		name = "Expanded",
		default = True
	)

	bake: BoolProperty(
		name = "Bake",
		description = "",
		default = True
	)

	key_all_bones: BoolProperty(
		name = "Key All Bones",
		description = "Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)",
		default = True
	)

	nla_strips: BoolProperty(
		name = "NLA Strips",
		description = "Export each non-muted NLA strip as a separated FBX’s AnimStack, if any, instead of global scene animation",
		default = True
	)

	all_actions: BoolProperty(
		name = "All Actions",
		description = "Export each action as a separated FBX’s AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)",
		default = True
	)

	force_keying: BoolProperty(
		name = "Force Start/End Keying",
		description = "Always add a keyframe at start and end of actions for animated channels",
		default = True
	)

	sampling_rate: FloatProperty(
		name = "Sampling Rate",
		description = "Sampling Rate, How often to evaluate animated values (in frames)",
		default = 1
	)

	simplify: FloatProperty(
		name = "Simplify",
		description="How much to simplify baked values (0.0 to disable, the higher the more simplified)",
		default = 1
	)


class QUICKEXPORTER_ExportPackageSettingsTextures(bpy.types.PropertyGroup):

	def copy_from(self, old):
		self.embed = old.embed
		self.path_mode = old.path_mode

	expanded: BoolProperty(
		name = "Expanded",
		default = True
	)

	embed: BoolProperty(
		name = "Embed Textures",
		description = "",
		default = False
	)

	path_mode: EnumProperty(
		name="Path Mode",
		description="Method used to reference paths for externally exported data. (Must be set to COPY for Embed Textures to work)",
		default="AUTO",
		items={
			("AUTO", "Auto", "Uses relative paths for files which are in a subdirectory of the exported location, absolute for any directories outside that.", "", 0),
			("ABSOLUTE", "Absolute", "Uses full paths.", "", 1),
			("RELATIVE", "Relative", "Uses relative paths in every case (except when on a different drive on Windows).", "", 2),
			("MATCH", "Match", "Uses relative / absolute paths based on the paths used in Blender.", "", 3),
			("STRIP", "Strip", "Only write the filename and omit the path component.", "", 4),
			("COPY", "Copy", "Copy the file on exporting and reference it with a relative path.", "", 5)
		}
	)


""" Package Export Settings """
class QUICKEXPORTER_ExportPackageSettings(bpy.types.PropertyGroup):

	def copy_from(self, old):
		self.include.copy_from(old.include)
		self.transform.copy_from(old.transform)
		self.geometry.copy_from(old.geometry)
		self.armature.copy_from(old.armature)
		self.animation.copy_from(old.animation)

	expanded: BoolProperty(
		name = "Expanded",
		default = True
	)

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

	textures: PointerProperty(
		name="Textures",
		type=QUICKEXPORTER_ExportPackageSettingsTextures
	)


""" Individual Package Data """
class QUICKEXPORTER_ExportPackage(bpy.types.PropertyGroup):

	def copy_from(self, old):
		self.name = old.name
		self.path = old.path

		'''Set Collection References Manually'''
		self.collections.clear()
		for c in old.collections:
			self.collections.add()
			self.collections[len(self.collections) - 1].pointer = c.pointer

		'''Set Object References Manually'''
		self.objects.clear()
		for o in old.objects:
			self.objects.add()
			self.objects[len(self.objects) - 1].pointer = o.pointer

		self.object_index = old.object_index
		self.settings.copy_from(old.settings)

	name: StringProperty(
		name="Name",
		default="Untitled Export Package"
	)

	path: StringProperty(
		name="Path",
		subtype="FILE_PATH",
		default="//",
		options={'PATH_SUPPORTS_BLEND_RELATIVE'}
	)

	objects: CollectionProperty(
		name="Objects",
		type=QUICKEXPORTER_ObjectPointer
	)

	collections: CollectionProperty(
		name="Collections",
		type=QUICKEXPORTER_CollectionPointer
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
	bpy.utils.register_class(QUICKEXPORTER_CollectionPointer)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsInclude)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsTransform)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsGeometry)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsArmature)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsAnimation)
	bpy.utils.register_class(QUICKEXPORTER_ExportPackageSettingsTextures)
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
	bpy.utils.unregister_class(QUICKEXPORTER_ExportPackageSettingsTextures)
	bpy.utils.unregister_class(QUICKEXPORTER_ExportPackageSettings)
	bpy.utils.unregister_class(QUICKEXPORTER_CollectionPointer)
	bpy.utils.unregister_class(QUICKEXPORTER_ObjectPointer)