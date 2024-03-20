import os
import base64
import pyttsx3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()

    if 'text' not in data:
        return jsonify({'error': 'Text field is missing'}), 400
    
    text = data['text']
    lang = data.get[lang]
    voice_type = data.get('voice_type', 'default')  # Default voice if not specified
    
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the language
    engine.setProperty('language', lang)

    # Get available voices for the selected language
    voices = engine.getProperty('voices')
    
    # Find a voice that matches the specified voice type
    selected_voice = None
    for voice in voices:
        if voice_type.lower() in voice.name.lower():
            selected_voice = voice
            break
    
    if selected_voice:
        engine.setProperty('voice', selected_voice.id)
    else:
        # If the specified voice type is not found, use the default voice
        print(f"Voice type '{voice_type}' not found for language '{lang}'. Using default voice.")

    # Save the audio as a temporary file
    audio_file = 'temp.mp3'
    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    
    # Read the audio content as binary
    with open(audio_file, 'rb') as f:
        audio_content = f.read()
    
    # Remove the temporary audio file
    os.remove(audio_file)
    
    # Encode audio content in base64
    audio_content_base64 = base64.b64encode(audio_content).decode('utf-8')
    
    return jsonify({'audio_content': audio_content_base64}), 200

if __name__ == '__main__':
    app.run(debug=True)
