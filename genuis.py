import time
import winsound as s
from mido import MidiFile
from beep import beep
import chippy
import pyaudio
from pathlib import Path
import asyncio
import threading

mid = MidiFile('Pirates of the Caribbean - Hes a Pirate.mid')
synth = chippy.Synthesizer(framerate=44100)
square_pcm = synth.pulse_riff(length=3, frequency=183, duty_cycle=25)

#for i in range(300):
#    print("""\
#    imtesting wfhferfjiveoc
#    eeee """)
#    time.sleep(0.033)


frame = 0


player = ["Hero", 100, 10]
enemy = ["Freddy Fazbear", 100, 10] # (enemy_name, health, attack)
art = open('fail.txt').read() #current enemy ascii art
redraw = open('blank.txt').read()
bear_attack = enemy[2]
hero_attack = player[2]
block = enemy[2] - 5



class Music(threading.Thread):

    def __init__(self, function_that_downloads):
        threading.Thread.__init__(self)
        self.runnable = function_that_downloads

    def run(self):
        self.runnable()


def music():
    for msg in mid.play():
        if msg.type == 'note_on':
            #s.Beep(int((400 / 32) * (2 ** ((msg.note - 9) / 12))), 500)
            s.PlaySound(("wavefile" + str(msg.note) + ".wav"), s.SND_ASYNC)
        elif msg.type == 'note_off':
            s.PlaySound(None, s.SND_ALIAS)


def draw():
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
        

def Hero():
    print(redraw)
    print(art)
    print("a wild " + enemy[0] + " attacks!")
    print("enemy hp: " + str(enemy[1]))
    print("Hero: " + "HP " + str(player[1]) + " | " + "AP " + str(player[2]))

def ask():
    print("")
    print("CHOOSE YOUR ACT!")
    print("attack (1), defend (2), or item (3)")
    ask = input("ACT: ")
    if ask == "1" or ask == "attack":
        enemy[1] -= player[2]

art = open('bear.txt').read()
s.Beep(800, 100)
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.type == 'note_on':
            if not Path(("wavefile" + str(msg.note) + ".wav")).is_file():
                square_pcm = synth.pulse_riff(length=0.5, frequency=int((400 / 32) * (2 ** ((msg.note - 9) / 12))), duty_cycle=25)
                synth.save_wave(square_pcm, ("wavefile" + str(msg.note) + ".wav"))
 
draw()
art = open('bear.txt').read()
Hero()
thread = Music(music)
thread.start()
ask()
Hero()
ask()