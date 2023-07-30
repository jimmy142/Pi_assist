import os
from gtts import gTTS

def text_to_speech(text, output_file):
    # Create gTTS object and save the speech as an mp3 file
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

    # Use mpg123 to play the audio file
    os.system('mpg123 ' + output_file)

# Example usage
text = "Hello, what'syour name?"
output_file = "output.mp3"
text_to_speech(text, output_file)
