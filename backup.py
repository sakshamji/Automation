#importing libs
import playsound
import os
import speech_recognition as sr


#this script listen and play audio


r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data=''
        try:
          voice_data = r.recognize_google(audio)
          
        except sr.UnknownValueError:
            print('Sorry,I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data 
    

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
    print('Hi , which song you want to listen to?')

    song = record_audio()
    print(song)
    print('Alrigt then playing your song right away')
    playsound.playsound('Music/'+find_song(music_files,song))




