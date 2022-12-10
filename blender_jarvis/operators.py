import bpy
from revChatGPT.revChatGPT import Chatbot

chatbot = None

class SendPromptToChatgpt(bpy.types.Operator):
    """Send text prompt to Chatgpt"""
    bl_label = "Blender J.A.R.V.I.S."
    bl_idname = "blender_jarvis.send_prompt_to_chatgpt"

    def execute(self, context):
        print(type(bpy.context.scene.session_token))
        config = {
            # "email": "<YOUR_EMAIL>",
            # "password": "<YOUR_PASSWORD>"#,
            "session_token": bpy.context.scene.session_token, # Deprecated. Use only if you encounter captcha with email/password
            #"proxy": "<HTTP/HTTPS_PROXY>"
        }

        text_prompt = f'Generate Python code for Blender {bpy.app.version_string} with the following: {bpy.context.scene.input_text_prompt}. Output only the code without explanations'

        # if not bpy.context.scene.chatbot:
        global chatbot
        if not chatbot:
            chatbot = Chatbot(config, conversation_id=None)

        response = chatbot.get_chat_response(text_prompt, output="text")
        code_block = response['message'].split('```')[1]

        # print(response['message'])

        # Create a new text data block
        new_text_block = bpy.data.texts.new(bpy.context.scene.input_text_prompt)

        # Modify the text in the new text block
        new_text_block.write(code_block)

        # text = bpy.data.texts['some_file_name.py']   # if exists in blend
        ctx = bpy.context.copy()
        ctx['edit_text'] = new_text_block
        bpy.ops.text.run_script(ctx)


        return {'FINISHED'}