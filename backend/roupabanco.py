import psycopg2
from backend.Roupa import Roupa

class Roupabanco:
    def __init__(self):
        pass

    def get_all_roupa(self):
        conexao = psycopg2.connect(
            dbname='20231214010035',
            user='postgres',
            password='pabd',
            host='localhost',
            port=5432
        )
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM guardaroupa")
        result = cursor.fetchall()
        conexao.commit()

        listaroupa = []
        if result !=None:
            for roupa in result:
                peca = roupa[0]
                valor = roupa[1]
                marca = roupa[2]
                tamanho = roupa[3]
                codigo=roupa[5]
                ativo = roupa[4]
                roupa = Roupa(peca, valor, marca, tamanho, codigo,ativo)
                listaroupa.append(roupa)
        else:
            listaroupa=None
        return listaroupa

    def add_roupa(self, peca, valor, marca, tamanho,ativo):

        conexao = psycopg2.connect(
            dbname='20231214010035',
            user='postgres',
            password='pabd',
            host='localhost',
            port=5432
        )
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO guardaroupa(peca,valor,marca,tamanho,ativo) VALUES ('{peca}',{valor},'{marca}','{tamanho}','{ativo}')")
        conexao.commit()

    def delete_roupa(self, codigo):
      
        conexao = psycopg2.connect(
            dbname='20231214010035',
            user='postgres',
            password='pabd',
            host='localhost',
            port=5432
        )
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE guardaroupa SET ativo = 'false' WHERE codigo = {codigo}")
        conexao.commit()
        conexao.close()
            
    def atualizar(self,peca,valor,marca,tamanho,codigo):
        conexao=psycopg2.connect(dbname='20231214010035',
                                user='postgres',
                                password='pabd',
                                host='localhost',
                                port=5432)
        cursor= conexao.cursor()
        codigosql=F"UPDATE guardaroupa SET peca= '{peca}', valor={valor}, marca='{marca}', tamanho='{tamanho}' WHERE codigo={codigo}"
        cursor.execute(codigosql)
        conexao.commit()

