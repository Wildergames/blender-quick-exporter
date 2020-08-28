import bpy

class UnityFBXExporterObjectPointer(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name="Name",
        default="Object"
    )

    pointer: bpy.props.PointerProperty(
        name="Object",
        type=bpy.types.Object
    )

    def update(self, context):
        print("UPDATING!"); 

""" Individual Package Data """
class UnityFBXExporterPackage(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name="Name",
        default="Untitled Export Package")

    path: bpy.props.StringProperty(
        name="Path",
        subtype="FILE_PATH",
        default="/")

    objects: bpy.props.CollectionProperty(
        name="Objects",
        type=UnityFBXExporterObjectPointer)
        
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
class UnityFBXExporterData(bpy.types.PropertyGroup):
    packages: bpy.props.CollectionProperty(
        name="Packages",
        type=UnityFBXExporterPackage)

    package_index: bpy.props.IntProperty(
        name="List Index",
        default=0)


""" Registration """
def register():
    bpy.utils.register_class(UnityFBXExporterObjectPointer)
    bpy.utils.register_class(UnityFBXExporterPackage)
    bpy.utils.register_class(UnityFBXExporterData)

    bpy.types.Scene.unity_fbx_exporter = bpy.props.PointerProperty(type=UnityFBXExporterData)

def unregister():
    bpy.utils.unregister_class(UnityFBXExporterPackage)
    bpy.utils.unregister_class(UnityFBXExporterData)
    bpy.utils.unregister_class(UnityFBXExporterObjectPointer)