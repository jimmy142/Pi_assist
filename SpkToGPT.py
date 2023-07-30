import speech_recognition as sr
from gtts import gTTS
import tempfile
import subprocess
import openai

openai.api_key = "sk- Add API key here"  # replace with your OpenAI key

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        filename = fp.name + ".mp3"
        tts.save(filename)
        print("mpg123 output:")
        print(subprocess.check_output(['mpg123', '-q', filename]))

def generate_gpt3_response(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    try:
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat_completion["choices"][0]["message"]["content"]
        return reply
    except Exception as e:
        print("Sorry, I could not generate a response.")
        print("Exception: " + str(e))
        return ""

def get_question(r, source):
    while True:  # Loop until a non-empty question is recognized
        audio_text = r.listen(source, timeout=5)  # Listen for up to 5 seconds
        try:
            question = r.recognize_google(audio_text)
            if question:  # If a non-empty string is recognized, return it as the question
                return question
        except sr.WaitTimeoutError:
            continue  # If no speech is detected within the timeout, listen again
        except Exception as e:
            print("Sorry, I did not get that.")
            print("Exception: " + str(e))

def speech_to_text():
    r = sr.Recognizer()
    print("Waiting for the trigger word: 'hey'...")

    while True:
        with sr.Microphone() as source:
            audio_text = r.listen(source)
        try:
            recognized_text = r.recognize_google(audio_text)
            print("Recognized Text: " + recognized_text)
            if recognized_text.lower().startswith('hey'):
                while True:  # Keep listening for questions until 'exit' is heard
                    print("Trigger word detected. Listening for the question...")
                    with sr.Microphone() as source:
                        question = get_question(r, source)
                        if question.lower() == 'exit':
                            print("Exit command recognized. Stopping.")
                            return
                        print("Recognized Question: " + question)
                        response = generate_gpt3_response(question)
                        print("Generated response: " + response)
                        text_to_speech(response, 'en')
                        print("Waiting for your next question...")
        except Exception as e:
            print("Sorry, I did not get that.")
            print("Exception: " + str(e))

if __name__ == "__main__":
    speech_to_text()