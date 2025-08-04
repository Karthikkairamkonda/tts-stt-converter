import gradio as gr
from gtts import gTTS
import speech_recognition as sr

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    output_path = "tts_output.wav"
    tts.save(output_path)
    return output_path

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return text
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("## 🎙️ TTS to STT Converter")

    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(label="Enter Text", placeholder="Type something to convert to speech")
            tts_button = gr.Button("🔊 Convert to Speech")
            audio_output = gr.Audio(label="TTS Output (.wav)")

        with gr.Column():
            audio_input = gr.Audio(label="Upload Audio for STT", type="filepath")
            stt_button = gr.Button("🧠 Convert to Text")
            text_output = gr.Textbox(label="Recognized Text")

    tts_button.click(fn=text_to_speech, inputs=text_input, outputs=audio_output)
    stt_button.click(fn=speech_to_text, inputs=audio_input, outputs=text_output)

demo.launch()