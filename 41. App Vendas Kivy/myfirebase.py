import requests
from kivy.app import App

class MyFirebase():
    API_KEY = "AIzaSyBVuZWmbY_QObDZ9i9Jn5LV2euYAt-me0E"

    def criar_conta(self, email, senha):
        link = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.API_KEY}"
        #print(email, senha)

        info = {"email": email,
                "password": senha,
                "returnSecureToken": True}
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()
        print(requisicao_dic)

        if requisicao.ok:
            print("Usuário Criado")
            #requisicao_dic["kind"] #não serve para o que está sendo feito
            #requisicao_dic["email"] #já tenho essa informação
            #requisicao_dic["idToken"] #autenticação. Serve para criar regras de restrição e visualização do banco de dados
            #requisicao_dic["refreshToken"] #token que mantém o usuário logado
            #requisicao_dic["expiresIn"] #padrão de 1 hora para expirar
            #requisicao_dic["localId"] #id_usuário que será criado no banco de dados

            refresh_token = requisicao_dic["refreshToken"]
            local_id = requisicao_dic["localId"]
            id_token = requisicao_dic["idToken"]

            meu_aplicativo = App.get_running_app()
            meu_aplicativo.local_id = local_id
            meu_aplicativo.id_token = id_token

            with open("refreshtokken.txt","w") as arquivo:
                arquivo.write(refresh_token)

        else:
            mensagem_erro = requisicao_dic["error"]["message"]
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids["login_page"]
            pagina_login.ids["mensagem_login"].text = mensagem_erro
            pagina_login.ids["mensagem_login"].color = (1, 0, 0, 1)
    def fazer_login(self, email, senha):
        pass 