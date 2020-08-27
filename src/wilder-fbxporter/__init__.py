
bl_info = {
        "name": "Unity FBX Exporter",
        "description": "Allows for the creation and exporting of custom FBX packages to Unity",
        "author": "Wilder Games Inc.",
        "version": (1, 0),
        "blender": (2, 80, 0),
        "location": "Properties > Scene > Unity FBX Exporter",
        "support": "COMMUNITY",
        "category": "Import-Export"
        }

import bpy
from . import ui
from . import operators
from . import properties


def register():
    properties.register()
    operators.register()
    ui.register()


def unregister():
    properties.unregister()
    operators.unregister()
    ui.unregister()

if __name__ == "__main__":
    register()
