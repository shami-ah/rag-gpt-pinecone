import os
import gradio as gr
import tempfile

# Save API key globally (or to a file if needed)
user_api_key = ""

# Dummy process function (replace with your real pipeline)
def process_file(file, question, api_key):
    global user_api_key
    user_api_key = api_key or user_api_key

    if not user_api_key:
        return "Please provide your API Key."

    # Simulate processing
    with open(file.name, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dummy answer
    answer = f"[ANSWER] Based on file content: '{content[:100]}...' and question: '{question}'"
    return answer

with gr.Blocks() as demo:
    gr.Markdown("# 🔐 Upload & Ask AI")
    api_key = gr.Textbox(label="Enter Your API Key", type="password")
    file_input = gr.File(label="Upload Your File")
    question = gr.Textbox(label="Ask a Question")
    output = gr.Textbox(label="Answer")

    submit_btn = gr.Button("Run")
    submit_btn.click(fn=process_file, inputs=[file_input, question, api_key], outputs=output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)