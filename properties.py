import bpy    
from revChatGPT.revChatGPT import Chatbot

class MDMToBlenderProperties(bpy.types.PropertyGroup):
    bpy.types.Scene.session_token = bpy.props.StringProperty(
        name="Session token",
        description="Session authentication token",
        subtype='PASSWORD'
    )

    bpy.types.Scene.input_text_prompt = bpy.props.StringProperty(
        name="ChatGPT prompt",
        description="Text prompt for ChatGPT"
    )

