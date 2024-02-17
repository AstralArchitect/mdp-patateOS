from sense_hat import SenseHat
import os

sense = SenseHat()
character = ["0", "0", "0", "0"]
message = "Veuillez saisir votre mot de passe"
sense.show_message(message, text_colour=(127, 127, 127), scroll_speed=0.1)
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
    sense.show_message(character[i], text_colour=(127, 127, 127), scroll_speed=0.1)
mdp = open("/root/mdp", "w")
mdp.write(character[0] + character[1] + character[2] + character[3])
mdp.close()
os.system("sudo rm -r /mdp/ ; sudo mkdir /mdp/ ; sudo git clone https://github.com/AstralArchitect/mdp-patateOS /mdp/ ; sudo mv /mdp/start/rc.local /etc/rc.local ; sudo rm -r /mdp/app/")