from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from hoverable import HoverBehavior
import json, glob
from datetime import datetime
from pathlib import Path
import random

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    def forgot_passwrd(self):
        self.manager.current = "forgot_password"
    def login(self,uname,pwrd):
        with open("users.json") as file:
            users = json.load(file)
            if uname in users and pwrd in users[uname]["password"] == pwrd:
                self.manager.current = "login_success"
            else:
                self.ids.wrong_details.text = "Wrong username or password"


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

#this has been added as kivy doesn't recognise Signupscreen library
#Hence a class needs to be defined in the python file
#this is similar to LoginScreen
class SignUpScreen(Screen):
    def add_user(self,uname,pwrd):
        with open("users.json") as file:
            users = json.load(file)
    
        users[uname]={"username":uname, "password": pwrd, 
        "created":datetime.now().strftime("%Y-%m-%d-%H-%m-%S")}

        with open("users.json","w") as file:
            json.dump(users, file)
            self.manager.current = "sign_up_success"

class SignUpSuccess(Screen):
    def login_page(self):
        #Controlling the transition of page switches
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen" 

class ForgotPassword(Screen):
    def retrieve_password(self, user):
        with open("users.json") as file:
            users = json.load(file)
            users1 = users[user]
            self.ids.passw.text = users1["password"]

    def main_page(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen" 

class LoginSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen" 

    def get_quote(self,feel):
        feel=feel.lower()
        available_feeling = glob.glob("quotes/*txt")
        available_feeling = [Path(filename).stem 
                            for filename in available_feeling]
        
        if feel in available_feeling:
            with open(f"quotes/{feel}.txt") as file:
                #print(file)
                quotes=file.readlines()
                #print(quotes)
                self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "We are trying to gauge you better! Till then try another feeling"

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass    

if __name__=="__main__":
    MainApp().run()