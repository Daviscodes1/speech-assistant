import speech_recognition as sr
import webbrowser
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTs

r = sr.Recognizer() #initializing recognizer

def record_audio(ask = False):
    with sr.Microphone() as source: #set microphone as input
        if ask:
            v_speak(ask)
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            v_speak('Sorry, I did not get that')
        except sr.RequestError:
            v_speak('Sorry, my speech service is down')
        return voice_data
    
def v_speak(audio_string):
    tts = gTTs(text=audio_string, lang='en')
    r = random.randimt(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
def respond(voice_data):
    if 'whats your name' in voice_data:
        v_speak('my name is V')
    if 'what time is it' in voice_data:
        v_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        v_speak('Here is what i found for' + search)
    if 'find location' in voice_data:
        location = record_audio('what location do you want to search for')
        url = 'https://google.nl/maps/place/' + location +'/&amp;'
        webbrowser.get().open(url)
        v_speak('Here is what i found for' + location)

    if 'exit' in voice_data:
        v_speak('Goodbye')
        exit()

time.sleep(1)
v_speak('How can i help you?')
while 1:
        voice_data = record_audio()
        v_speak(voice_data)
        respond(voice_data)