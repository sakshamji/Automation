#importing libs
import playsound
import os


#this script play audio based on keyboard input
# to stop just give keyboard interrupt for now     

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

song = input('Hi , which song you want to listen to?\n')

print ('Alrigt then playing your song right away')
playsound.playsound('Music/'+find_song(music_files,song))




