#importing libs
import playsound
import os
import speech_recognition as sr
from gtts import gTTS

#this is complete voice assisst audio player
import random
import multiprocessing

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            Assis_speak(ask)
        audio = r.listen(source)
        voice_data=''
        try:
          voice_data = r.recognize_google(audio)
          
        except sr.UnknownValueError:
            Assis_speak('Sorry,I did not get that')
        except sr.RequestError:
            Assis_speak('Sorry, my speech service is down')
        return voice_data 
def Assis_speak(audio_string):
    tts = gTTS(audio_string)
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)    
    os.remove(audio_file)      

def get_files():
    return os.listdir('Music')

def find_song(music_files,song):
    song = song.lower()
    for file_name in music_files:
        if (file_name.lower()).find(song)!=-1:
            return file_name
    return 'not found'

# playsound(path)
music_files = get_files()
while(1):
    Assis_speak('Hi , which song you want to listen to?')

    song = record_audio()
    print()
    Assis_speak('Alrigt then playing your song right away')
    playsound.playsound('Music/'+find_song(music_files,song))




