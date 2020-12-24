from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_message
import random

height = 175.8
weight = 89.7
bmi = 29.1
remind_data = [
    "The weather is cold, put some more clothes to keep yourself warm.\nend of remind mode, please enter start",
    "It's cold out, make sure you're warm.\nend of remind mode, please enter start",
    "The weather is cold please much adds clothes.\nend of remind mode, please enter start",
    "It's getting cold outside, keep yourself warm.\nend of remind mode, please enter start",
    "The weather became cold, remembering more a clothes.\nend of remind mode, please enter start"
]
cheerup_data = [
    "https://i.imgur.com/qAJQbJo.jpg",
    "https://i.imgur.com/i07HQNi.jpg",
    "https://i.imgur.com/b886Q2g.jpg",
    "https://i.imgur.com/dtXebGA.jpg",
]


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_military(self, event):
        text = event.message.text
        return text.lower() == "military"

    def is_going_to_female(self, event):
        text = event.message.text
        return text.lower() == "female"

    def is_going_to_male(self, event):
        text = event.message.text
        return text.lower() == "male"

    def is_going_to_tall(self, event):
        text = event.message.text
        height = float(text)
        print(height)
        return (height > 157 and height < 196)

    def is_going_to_tall_ex(self, event):
        text = event.message.text
        height = float(text)
        print(height)
        return not(height > 157 and height < 196)

    def is_going_to_Military_service(self, event):
        text = event.message.text
        weight = float(text)
        print(weight)
        bmi = weight / (height/100) / (height/100)
        print(bmi)
        return (bmi >= 17 and bmi <= 31)

    def is_going_to_Alternative(self, event):
        text = event.message.text
        weight = float(text)
        print(weight)
        bmi = weight / (height/100) / (height/100)
        print(bmi)
        return ((bmi > 31 and bmi <= 31.5) or (bmi >= 16.5 and bmi < 17))

    def is_going_to_Exemption(self, event):
        text = event.message.text
        weight = float(text)
        print(weight)
        bmi = weight / (height/100) / (height/100)
        print(bmi)
        return (bmi > 31.5 or bmi < 16.5)

    def is_going_to_remind(self, event):
        text = event.message.text
        return text.lower() == "remind"

    def is_going_to_cheerup(self, event):
        text = event.message.text
        return text.lower() == "cheerup"


# on enter function


    def on_enter_start(self, event):
        print("I'm entering start")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "Start! please choose the mode \n1. Enter military\n2. Enter remind\n3. Enter cheerup")

    def on_enter_military(self, event):
        print("I'm entering military")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "Welcome to the military mode!\nWhat's your gender? female/male")

    def on_enter_female(self, event):
        print("I'm entering female")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "CONGRATULATIONS!! You don't need to do the mandatory military service\nend of military mode, please enter start")
        self.go_back()

    def on_enter_male(self, event):
        print("I'm entering male")
        reply_token = event.reply_token
        send_text_message(reply_token, "How tall are you?")

    def on_enter_tall(self, event):
        print("I'm entering tall")
        reply_token = event.reply_token
        send_text_message(reply_token, "What is your weight?")

    def on_enter_tall_ex(self, event):
        print("I'm entering tall_ex")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "CONGRATULATIONS!! You don't need to do the mandatory military service\nend of military mode, please enter start")
        self.go_back()

    def on_enter_Military_service(self, event):
        print("I'm entering Military_service")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "OH NO!!! You should do the mandatory military service\nend of military mode, please enter start")
        self.go_back()

    def on_enter_Alternative(self, event):
        print("I'm entering Alternative")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "OKAY! You should do the Alternative military service\nend of military mode, please enter start")
        self.go_back()

    def on_enter_Exemption(self, event):
        print("I'm entering Exemption")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "CONGRATULATIONS!! You are exemption from military service\nend of military mode, please enter start")
        self.go_back()

    def on_enter_remind(self, event):
        print("I'm entering remind")
        reply_token = event.reply_token
        send_text_message(
            reply_token, remind_data[random.randint(0, 4)])
        self.go_back()

    def on_enter_cheerup(self, event):
        print("I'm entering cheerup")
        reply_token = event.reply_token
        send_image_message(
            reply_token, cheerup_data[random.randint(0, 3)])
        self.go_back()
