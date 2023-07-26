from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("main.kv")

class MAinApp(App):
    def build(self):
        return GUI
    
MAinApp().run()