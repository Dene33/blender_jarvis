import bpy    
from revChatGPT.revChatGPT import Chatbot

class MDMToBlenderProperties(bpy.types.PropertyGroup):
    session_token: bpy.props.StringProperty(
        name="Session token",
        description="Session authentication token",
        subtype='PASSWORD'
    )

    email: bpy.props.StringProperty(
        name="E-mail",
        description="E-mail used for registration in ChatGPT",
    )

    password: bpy.props.StringProperty(
        name="Password",
        description="Password used for registration in ChatGPT",
        subtype='PASSWORD'
    )

    input_text_prompt: bpy.props.StringProperty(
        name="ChatGPT prompt",
        description="Text prompt for ChatGPT"
    )

    auth_method: bpy.props.EnumProperty(
        name="Authentication method",
        items=[
            ("PASSWORD", "Email, Password", "Authentication with e-mail and password"),
            ("TOKEN", "Session Token", "Authentication with session token")
        ],
        default="PASSWORD"
    )

    def register():
        bpy.types.Scene.blender_jarvis = bpy.props.PointerProperty(type=MDMToBlenderProperties)

    def unregister():
        del bpy.context.scene.blender_jarvis

