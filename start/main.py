from sense_hat import SenseHat
import os
from time import sleep

sense = SenseHat()
character = ["0", "0", "0", "0"]
trueMdp = ["0", "0", "0", "0"]
mdp = open("/root/mdp", "r")
TrueMdp = mdp.read()
for i in range(4):
    trueMdp[i] = TrueMdp[i]
mdp.close()
ok = False
message = "mdp ?"
sense.show_message(message, text_colour=(0, 0, 127), scroll_speed=0.1)
for i in range(4):
    a = 0
    while a == 0:
        events = sense.stick.get_events()
        for event in events:
            if event.action == "pressed" and event.direction == "up":
                character[i] = "0"
                a = 1
                break
            elif event.action == "pressed" and event.direction == "down":
                character[i] = "1"
                a = 1
                break
            elif event.action == "pressed" and event.direction == "left":
                character[i] = "2"
                a = 1
                break
            elif event.action == "pressed" and event.direction == "right":
                character[i] = "3"
                a = 1
                break
for i in range(4):
    if(character[i] == trueMdp[i]):
        continue
    else:
        message = "arret..."
        sense.show_message(message, text_colour=(127, 0, 0), scroll_speed=0.1)
        sleep(0.5)
        os.system("sudo shutdown now")
os.system("sudo sh /root/strat.sh")