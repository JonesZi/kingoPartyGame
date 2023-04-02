# Importing kivy classes as parent classes for everything we will do in the app
from kivy.app import App
from kivy.uix.button import Button

# Creating the App class - always is a child class of kivy.App
class LanguageLearnerApp(App):
    # Building the app, ie adding widgets
    def build(self):
        return Button(
            text="Hello World",
            pos=(50,50),
            size_hint=(0.8,0.8)
            )

if __name__=="__main__":
    LanguageLearnerApp().run()

