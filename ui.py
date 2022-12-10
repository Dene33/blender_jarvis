import bpy
from properties import MDMToBlenderProperties

class BlenderJarvisPanel(bpy.types.Panel):
    bl_label = "Blender J.A.R.V.I.S."
    bl_idname = "OBJECT_PT_blender_jarvis_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Blender J.A.R.V.I.S."

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.blender_jarvis, "auth_method")

        if bpy.context.scene.blender_jarvis.auth_method == 'TOKEN':
            # Create a auth token
            layout.prop(context.scene.blender_jarvis, "session_token")
        elif bpy.context.scene.blender_jarvis.auth_method == 'PASSWORD':
            layout.prop(context.scene.blender_jarvis, "email")
            layout.prop(context.scene.blender_jarvis, "password")

        # Create a text input field
        layout.prop(context.scene.blender_jarvis, "input_text_prompt")

        # Create a button
        layout.operator("blender_jarvis.send_prompt_to_chatgpt")
        # layout.operator("mdm_to_blender.send_prompt_to_mdm.cancel")