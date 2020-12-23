from transitions.extensions import GraphMachine

from utils import send_text_message

height = 175.8
weight = 89.7
bmi=29.1
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
        return (height > 0 and height < 300)
    def is_going_to_Military_service(self, event):
        text = event.message.text
        weight = float(text)
        print(weight)
        bmi = weight / (height/100) / (height/100)
        print(bmi)
        return (bmi>=17 and bmi<=31)
    def is_going_to_Alternative(self, event):
        text = event.message.text
        weight = float(text)
        print(weight)
        bmi = weight / (height/100) / (height/100)
        print(bmi)
        return ((bmi>31 and bmi<=31.5) or (bmi>=16.5 and bmi<17) )
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

    def on_enter_start(self, event):
        print("I'm entering start")
        reply_token = event.reply_token
        send_text_message(reply_token, "Start! please choose the mode \n1. Enter military\n2. Enter remind")
#mode military
    def on_enter_military(self, event):
        print("I'm entering military")
        reply_token = event.reply_token
        send_text_message(reply_token, "Welcome to the military mode!\nWhat's your gender? female/male")
    def on_enter_female(self, event):
        print("I'm entering female")
        reply_token = event.reply_token
        send_text_message(reply_token, "CONGRATULATIONS!! You don't need to do the mandatory military service\nend of military mode, please enter start")
        self.go_back()
    def on_enter_male(self, event):
        print("I'm entering male")
        reply_token = event.reply_token
        send_text_message(reply_token, "How tall are you?")
    def on_enter_tall(self, event):
        print("I'm entering tall")
        reply_token = event.reply_token
        send_text_message(reply_token, "What is your weight?")
    def on_enter_Military_service(self, event):
        print("I'm entering Military_service")
        reply_token = event.reply_token
        send_text_message(reply_token, "OH NO!!! You should do the mandatory military service\nend of military mode, please enter start")
        self.go_back()
    def on_enter_Alternative(self, event):
        print("I'm entering Alternative")
        reply_token = event.reply_token
        send_text_message(reply_token, "OKAY! You should do the Alternative military service\nend of military mode, please enter start")
        self.go_back()
    def on_enter_Exemption(self, event):
        print("I'm entering Exemption")
        reply_token = event.reply_token
        send_text_message(reply_token, "CONGRATULATIONS!! You are exemption from military service\nend of military mode, please enter start")
        self.go_back()
#mode military end
    def on_enter_remind(self, event):
        print("I'm entering remind")
        reply_token = event.reply_token
        send_text_message(reply_token, "The weather is cold, put some more clothes to keep yourself warm.\nend of remind mode, please enter start")
        self.go_back()
    def on_enter_error(self, event):
        print("I'm entering error")
        reply_token = event.reply_token
        send_text_message(reply_token, "error please try again")
        self.go_back()

