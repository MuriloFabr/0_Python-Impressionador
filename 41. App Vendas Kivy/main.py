#IMPORTANDO TODAS AS BIBLIOTECAS QUE SERÃO UTILIZADAS
from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *


#FUNÇÃO PRINCIPAL QUE RODA O APP
GUI = Builder.load_file("main.kv")

class MAinApp(App):
    def build(self):
        return GUI
    
    def mudar_tela(self,id_tela):
        #print(self.root.ids)    #Dicionário de todos os ids que existem dentro do Gerenciador de Telas
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

    
MAinApp().run()