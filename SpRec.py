import speech_recognition as sr

def speech_to_text():
    # Create a recognizer object
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    try:
        # Use Google Web Speech API to recognize the audio
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Example usage
speech_to_text()


