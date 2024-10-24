import psycopg2

class Roupa:
    def __init__(self, peca, valor, marca,tamanho,codigo,ativo=None):
        self.peca = peca
        self.valor = valor
        self.marca = marca
        self.ativo=ativo
        self.tamanho = tamanho
        self.codigo = codigo

    def __str__(self):
        return (f"peca: {self.peca}\n"
                f"Valor: R${self.valor}\n"
                f"Marca: {self.marca}\n"
                f"Tamanho: {self.tamanho}\n"
                f"Código: {self.codigo}")