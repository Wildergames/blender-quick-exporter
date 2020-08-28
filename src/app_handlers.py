import bpy
from bpy.app.handlers import persistent

@persistent
def on_save(dummy):
	print('Quick Exporter: File was saved. Should Auto-Export run?')
	if(bpy.context.scene.quick_exporter.auto_export == "DISABLED"):
		print("Quick Exporter: Auto-Export is disabled")
	else:
		print("Quick Exporter: Auto-Export is enabled")
		bpy.ops.quick_exporter.export_all()


""" Registration """
def register():
	if not on_save in bpy.app.handlers.save_post:
		bpy.app.handlers.save_post.append(on_save)

def unregister():
	if on_save in bpy.app.handlers.save_post:
		bpy.app.handlers.save_post.remove(on_save)