import time
import winsound as s
from mido import MidiFile

mid = MidiFile('Tarrega_Adelita.mid')

#for i in range(300):
#    print("""\
#    imtesting wfhferfjiveoc
#    eeee """)
#    time.sleep(0.033)


player = ["Hero", 100, 10]
enemy = ["Freddy Fazbear", 100, 10] # (enemy_name, health, attack)
art = open('fail.txt').read() #current enemy ascii art
redraw = open('blank.txt').read()
bear_attack = enemy[2]
hero_attack = player[2]
block = enemy[2] - 5

def draw():
    print(redraw)
    print(art)
    print("a wild " + enemy[0] + " attacks!")
    print("enemy hp: " + str(enemy[1]))

def Hero():
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
for msg in mid.play():
    if msg
draw()
Hero()
ask()