class Fornecedor:
    def __init__(self,nomeforn,codigoprod,codigoforn):
       self.nomeforn=nomeforn
       self.codigoprod=codigoprod
       self.codigoforn=codigoforn

    def __str__(self):
       return f"nomedofornecedor:{self.nomeforn}\ncodigoproduto{self.codigoprod}\ncodigodofornecedor:{self.codigoforn}"