import psycopg2
from backend.Fornecedor import Fornecedor

class FornecedorBanco:
    def __init__(self) -> None:
        pass        
    def get_all_fornecedores(self):
        conexao = psycopg2.connect(
            dbname='20231214010035',
            user='postgres',
            password='pabd',
            host='localhost',
            port=5432
        )
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM fornecedor")
        result = cursor.fetchall()
        conexao.commit()

        listafornecedor = []
        if result !=None:
            for fornecedor in result:
                nomeforn = fornecedor[0]
                codigoprod = fornecedor[1]
                codigoforn = fornecedor[2]
                fornecedor = Fornecedor(nomeforn, codigoprod, codigoforn)
                listafornecedor.append(fornecedor)
        else:
            listafornecedor=None
        return listafornecedor

    def vendeproduto (self,codigoproduto,codigofornecedor):
        conexao = psycopg2.connect(
            dbname='20231214010035',
            user='postgres',
            password='pabd',
            host='localhost',
            port=5432
        )
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE fornecedor SET codigoproduto={codigoproduto} WHERE codigofornecedor={codigofornecedor}")
