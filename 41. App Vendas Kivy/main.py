#IMPORTANDO TODAS AS BIBLIOTECAS QUE SERÃO UTILIZADAS
from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
import requests


#FUNÇÃO PRINCIPAL QUE RODA O APP
GUI = Builder.load_file("main.kv")

class MainApp(App):
    id_usuario = 1 #definindo manualmente o usuário, sem estar fazendo tela de login ainda

    def build(self):
        return GUI
    

    def on_start(self):
        #requisicao = requests.get("https://hashtag-app-vendas-default-rtdb.firebaseio.com/.json") #sempre colocar .json no final do link
        #print(requisicao.json()) #essencialmente a requisição vira um arquivo .json do python. Aqui está puxando o banco inteiro ainda

        requisicao = requests.get(f"https://hashtag-app-vendas-default-rtdb.firebaseio.com/{self.id_usuario}.json") #olhar módulo de Orientação a objetos para entender porque chamar a variável com o self
        #print(requisicao.json()) #aqui está puxando apenas o dicionário do usuário pretendido
        requisicao_dic = requisicao.json()
        #print(requisicao_dic)
        avatar = requisicao_dic["avatar"]
        #print(avatar)
        #print(self.root.ids) #todos os ids que existem no nosso arquivo main do programa
        foto_superior = self.root.ids["foto_superior"]
        foto_superior.source = f"icones/fotos_perfil/{avatar}"
    

    def mudar_tela(self,id_tela):
        #print(self.root.ids)    #Dicionário de todos os ids que existem dentro do Gerenciador de Telas
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

    
MainApp().run()