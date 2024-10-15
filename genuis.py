import multiprocessing
from random import randint, randrange
import random
import time
import winsound as s
from mido import bpm2tempo, tick2second, MidiFile
import chippy
from pathlib import Path
#import threading
import simpleaudio as sa
import wave
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
from pydub.playback import play as audi
import keyboard
import asyncio
import msvcrt as m
from multiprocessing import Process, freeze_support, get_context, set_start_method, get_all_start_methods
import os


mid = MidiFile('Tarrega_Adelita.mid')
synth = chippy.Synthesizer(framerate=48000)
square_pcm = synth.pulse_riff(length=3, frequency=183, duty_cycle=25)



#for i in range(300):
#    print("""\
#    imtesting wfhferfjiveoc
#    eeee """)
#    time.sleep(0.033)


frame = 0

note = {}
play = {}

player = ["Hero", int(open('diff.txt').readlines()[2]), 10]
enemy = ["Freddy Fazbear", int(open('diff.txt').readlines()[1]), int(open('diff.txt').readlines()[0])] # (enemy_name, health, attack)
art = open('fail.txt').read() #current enemy ascii art
redraw = open('blank.txt').read()
bear_attack = enemy[2]
hero_attack = player[2]
block = enemy[2] - 5
done = False

"""
class Music(threading.Thread):

    def __init__(self, function_that_downloads):
        threading.Thread.__init__(self)
        self.runnable = function_that_downloads

    def run(self):
        self.runnable()
"""

def music():
    time.sleep(2.3)
    for msg in mid.play():
        if msg.type == 'note_on':
            mus = note[msg.note]
            play[msg.note] = _play_with_simpleaudio(mus + ((msg.velocity - 64) * 0.5))
            #s.Beep(int((400 / 32) * (2 ** ((msg.note - 9) / 12))), 500)
            #s.PlaySound(("wavefile" + str(msg.note) + ".wav"), s.SND_ASYNC)
            #note = sa.WaveObject.from_wave_file(("wavefile" + str(msg.note) + ".wav"))
            #audio_data = note[msg.note].readframes(note[msg.note].getnframes())
            #num_channels = note[msg.note].getnchannels()
            #bytes_per_sample = note[msg.note].getsampwidth()
            #sample_rate = note[msg.note].getframerate()
            #play[msg.note] = sa.play_buffer(audio_data, num_channels, bytes_per_sample, sample_rate)
        #elif msg.type == 'note_off':
            #s.PlaySound(None, s.SND_ALIAS)
            play[msg.note].stop()

def draw():
    global done
    global frame
    global art
    print(redraw)
    print(art)
    #print("a wild " + enemy[0] + " attacks!")
    #print("enemy hp: " + str(enemy[1]))
    timeout = 2.3   # [seconds]
    timeout_start = time.time()
    s.PlaySound("bear_polar.wav", s.SND_ASYNC) 
    while time.time() < timeout_start + timeout:
        time.sleep(0.01)
        frame += 1
        if frame % 2 == 0:
            art = open('bear1.txt').read()
        else:
            art = open('bear.txt').read()
        print(redraw)
        print(art)
        

def dam(dam, defe=0):
    print("you took " + str(dam) + " amount of damage")
    if defe:
        print("you negated " + str(defe))
    global player
    
    player[1] -= dam

def Hero():
    print(redraw)
    print(art)
    print("a wild " + enemy[0] + " attacks!")
    print("enemy hp: " + str(enemy[1]) + " | dmg: " + str(enemy[2]))
    print("Hero: " + "HP " + str(player[1]))

def ask():
    print("")
    seep = 1.3
    print("CHOOSE YOUR ACT!")
    print("attack (1), or defend (2)?")
    m.getch()
    roll = random.randint(0, 4)
    #print(roll)
    if roll == 1:
        player[2] = random.randint(9, 16)
        for i in range(10):
            print("it's a crit!!")
        seep = 1.5
    else:
        player[2] = randint(8, 10)
    if keyboard.is_pressed('1'):
        enemy[1] -= player[2]
        s.PlaySound('Explosion6', s.SND_NODEFAULT)
        print("you attack with " + str(player[2]))
        dam(enemy[2])
        time.sleep(seep)
    if keyboard.is_pressed('2'):
        defe = random.randint(0, 4)
        dam(enemy[2] - defe, defe)
        time.sleep(seep)

art = open('bear.txt').read()


for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.type == 'note_on':
            if not Path(("wavefile" + str(msg.note) + ".wav")).is_file():
                square_pcm = synth.pulse_riff(length=0.5, frequency=int((400 / 32) * (2 ** ((msg.note - 9) / 12))), duty_cycle=25)
                synth.save_wave(square_pcm, ("wavefile" + str(msg.note) + ".wav"))
            note[msg.note] = AudioSegment.from_wav(("wavefile" + str(msg.note) + ".wav"), 'rb')
art = open('bear.txt').read()
print(get_all_start_methods())
#done = True
if __name__ == '__main__':
    freeze_support()
    global thread
    thread = Process(target=music)
    thread.start()
    print("wajfsiuhjfhbnrsdiujhghbrfnug hjfdnbg ujsrf hgusrf ghry8u  gt")
draw()
Hero()
while enemy[1] >= 0:
    Hero()
    ask()
    if player[1] <= 0:
        thread.terminate()
        mid = MidiFile('marche.mid')
        note = {}
        play = {}
        for i, track in enumerate(mid.tracks):
            print('Track {}: {}'.format(i, track.name))
            for msg in track:
                if msg.type == 'note_on':
                    if not Path(("wavefile" + str(msg.note) + ".wav")).is_file():
                       square_pcm = synth.pulse_riff(length=0.5, frequency=int((400 / 32) * (2 ** ((msg.note - 9) / 12))), duty_cycle=25)
                       synth.save_wave(square_pcm, ("wavefile" + str(msg.note) + ".wav"))
                    note[msg.note] = AudioSegment.from_wav(("wavefile" + str(msg.note) + ".wav"), 'rb')
        for i in range(100):
            print("you lose!!!!")
        music()
        exit(None)
        
print("you winnn, yay")
for i in range(100):
    print("you winnn, yay")

thread.terminate()
mid = MidiFile('Tetris - B Theme.mid')
note = {}
play = {}
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.type == 'note_on':
            if not Path(("wavefile" + str(msg.note) + ".wav")).is_file():
                square_pcm = synth.pulse_riff(length=0.5, frequency=int((400 / 32) * (2 ** ((msg.note - 9) / 12))), duty_cycle=25)
                synth.save_wave(square_pcm, ("wavefile" + str(msg.note) + ".wav"))
            note[msg.note] = AudioSegment.from_wav(("wavefile" + str(msg.note) + ".wav"), 'rb')

music()