
bl_info = {
        "name": "Quick Exporter",
        "description": "Allows for the quick creation and exporting of custom FBX packages",
        "author": "Wilder Games Inc.",
        "version": (1, 0),
        "blender": (2, 80, 0),
        "location": "Properties > Scene > Quick Exporter",
        "support": "COMMUNITY",
        "category": "Import-Export"
        }

import bpy
import importlib
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

def reload():
    properties.reload()
    operators.reload()
    ui.reload()



if __name__ == "__main__":
    register()


