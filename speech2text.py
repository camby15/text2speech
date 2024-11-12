import pyttsx3
import speech_recognition as sr

def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say something...!')
        audio = r.listen(source)  # listen for the data (load audio from microphone)
        print('done!')
        
    try:
        text = r.recognize_google(audio, language='en-US')   # recognize (convert from audio to text)
        print('you said'+ text)
        
    except Exception as e:
        print(e)


get()

