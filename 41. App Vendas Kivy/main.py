#IMPORTANDO TODAS AS BIBLIOTECAS QUE SERÃO UTILIZADAS
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


#DECLARANDO TODAS AS TELAS QUE SERÃO GERENCIADAS NO APP
class Home_Page(Screen):
    pass


#FUNÇÃO PRINCIPAL QUE RODA O APP
GUI = Builder.load_file("main.kv")

class MAinApp(App):
    def build(self):
        return GUI
    
MAinApp().run()