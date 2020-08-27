import bpy

class UNITYFBXEXPORTER_PT_ui(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_idname = "UNITYFBXEPORTER_PT_ui"
    bl_label = "Unity FBX Exporter"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene" 

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        box = layout.box()
        box.label(text="Package 1")
        
        box = layout.box()
        box.label(text="Package 2")
        
        box = layout.box()
        box.label(text="Package 3")
        
        """ Export All """
        row = layout.row()
        row.scale_y = 2.0
        row.operator("unity_fbx_exporter.export_all")
         

        """ EXAMPLES

        # Create a simple row.
        layout.label(text="Simple Row:")

        row = layout.row()
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

        # Create an row where the buttons are aligned to each other.
        layout.label(text=" Aligned Row:")

        row = layout.row(align=True)
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

        # Create two columns, by using a split layout.
        split = layout.split()

        # First column
        col = split.column()
        col.label(text="Column One:")
        col.prop(scene, "frame_end")
        col.prop(scene, "frame_start")

        # Second column, aligned
        col = split.column(align=True)
        col.label(text="Column Two:")
        col.prop(scene, "frame_start")
        col.prop(scene, "frame_end")

        # Big render button
        layout.label(text="Big Button:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("render.render")

        # Different sizes in a row
        layout.label(text="Different button sizes:")
        row = layout.row(align=True)
        row.operator("render.render")

        sub = row.row()
        sub.scale_x = 2.0
        sub.operator("render.render")

        row.operator("render.render")
        """

def register():
    bpy.utils.register_class(UNITYFBXEXPORTER_PT_ui)

def unregister():
    bpy.utils.unregister_class(UNITYFBXEXPORTER_PT_ui)