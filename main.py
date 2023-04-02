# Importing kivy classes as parent classes for everything we will do in the app
from kivy.app import App
from kivy.uix.button import Button

# Creating the App class - always is a child class of kivy.App
class LanguageLearnerApp(App):
    # Building the app, in this case with one widget - Button
    def build(self):
        return Button(text="Hello World")

if __name__=="__main__":
    LanguageLearnerApp().run()

