import bpy

# For more information about Blender Properties, visit:
# <https://blender.org/api/blender_python_api_2_78a_release/bpy.types.Property.html>
# from bpy.props import BoolProperty
# from bpy.props import CollectionProperty
# from bpy.props import EnumProperty
# from bpy.props import FloatProperty
# from bpy.props import IntProperty
# from bpy.props import PointerProperty
# from bpy.props import StringProperty
# from bpy.props import PropertyGroup

class UnityFBXExporterPackage(bpy.types.PropertyGroup):
    path: bpy.props.StringProperty(name="Path")
    scale: bpy.props.FloatProperty(name="Scale", default=1)
    applyTransform: bpy.props.BoolProperty("Apply Transform", default=True, description="Freeze all transforms on export. (EXPERIMENTAL!)") 
    applyModifiers: bpy.props.BoolProperty("Apply Modifiers", default=True, description="Applies all modifiers on export") 

class UnityFBXExporterData(bpy.types.PropertyGroup):
    #packages = bpy.props.CollectionProperty(type=UnityFBXExporterPackage)
    packages: bpy.props.PointerProperty(type=UnityFBXExporterPackage)


def register():
    bpy.utils.register_class(UnityFBXExporterPackage)
    bpy.utils.register_class(UnityFBXExporterData)
    bpy.types.Scene.fbxporter = bpy.props.PointerProperty(type=UnityFBXExporterData)

def unregister():
    bpy.utils.unregister_class(UnityFBXExporterPackage)
    bpy.utils.unregister_class(UnityFBXExporterData)