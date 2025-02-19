#IMPORTANDO TODAS AS BIBLIOTECAS QUE SERÃO UTILIZADAS
from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
from funcoes import *
import requests
from bannervenda import BannerVenda


#FUNÇÃO PRINCIPAL QUE RODA O APP
GUI = Builder.load_file("main.kv")

class MainApp(App):
    id_usuario = 1 #definindo manualmente o usuário, sem estar fazendo tela de login ainda

    def build(self):
        return GUI
    

    def on_start(self):

        ### Pegando o Dicionário de Dados de determinado usuário
        #requisicao = requests.get("https://hashtag-app-vendas-default-rtdb.firebaseio.com/.json") #sempre colocar .json no final do link
        #print(requisicao.json()) #essencialmente a requisição vira um arquivo .json do python. Aqui está puxando o banco inteiro ainda
        requisicao = requests.get(f"https://hashtag-app-vendas-default-rtdb.firebaseio.com/{self.id_usuario}.json") #olhar módulo de Orientação a objetos para entender porque chamar a variável com o self
        #print(requisicao.json()) #aqui está puxando apenas o dicionário do usuário pretendido
        requisicao_dic = requisicao.json()
        #print(requisicao_dic)

        ### Preencher Foto de Perfil
        avatar = requisicao_dic["avatar"]
        #print(avatar)
        #print(self.root.ids) #todos os ids que existem no nosso arquivo main do programa
        foto_superior = self.root.ids["foto_superior"]
        foto_superior.source = f"icones/fotos_perfil/{avatar}"

        ### Preencher Lista de Vendas
        try:
            vendas = requisicao_dic["vendas"][1:]
            for venda in vendas:
                # print(venda)
                banner = BannerVenda(cliente=venda["cliente"], foto_cliente=venda["foto_cliente"],
                                     produto=venda["produto"], foto_produto=venda["foto_produto"],
                                     data=venda["data"], preco=venda["preco_total"],
                                     unidade=venda["unidade"], quantidade=venda["quantidade"])
                pagina_homepage = self.root.ids["home_page"]
                # print(pagina_homepage.ids)
                lista_vendas = pagina_homepage.ids["lista_vendas"]
                lista_vendas.add_widget(banner)
        except:
            pass

    

    def mudar_tela(self,id_tela):
        #print(self.root.ids)    #Dicionário de todos os ids que existem dentro do Gerenciador de Telas
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

    
MainApp().run()