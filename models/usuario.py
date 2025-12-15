class Usuario:
    def __init__(self, nome, email, senha, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo  #que pode ser DOADOR ou BENEFICIARIO
