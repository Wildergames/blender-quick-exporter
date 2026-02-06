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


bl_info = {
	"name": "Quick Exporter",
	"author": "Tony Coculuzzi - Wilder Games",
	"description": "Create, manage, and export custom mesh packages",
	"version": (1, 2),
	"blender": (2, 80, 0),
	"location": "View3D > Sidebar > Quick Exporter",
	"support": "COMMUNITY",
	"category": "Import-Export"
	}

import bpy

# Check if scripts have already been imported
# If true, reload instead of importing
if "ui" not in locals():
	from . import properties, operators, app_handlers, ui
	print("Quick Exporter: Importing")
else:
	import importlib
	properties = importlib.reload(properties)
	operators = importlib.reload(operators)
	app_handlers = importlib.reload(app_handlers)
	ui = importlib.reload(ui)
	print("Quick Exporter: Reloading Scripts")

""" Registration """
def register():
	properties.register()
	operators.register()
	app_handlers.register()
	ui.register()

def unregister():
	properties.unregister()
	operators.unregister()
	app_handlers.unregister()
	ui.unregister()

if __name__ == "__main__":
	register()