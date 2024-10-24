class Usuario:
    def __init__(self,nome,senha,codigo):
        self.nome=nome
        self.senha=senha
        self.codigo=codigo
    def __str__(self) -> str:
        return f"Nome: {self.nome}\nSenha: {self.senha}\ncodigo: {self.codigo}"