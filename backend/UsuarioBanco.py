import psycopg2
from backend.Usuario import Usuario
class UsuarioBanco:
      def _ini_(self):
          pass
      def get_usuario_pelo_nome(self,nome):
        conexao=psycopg2.connect(dbname='20231214010035',
                                user='postgres',
                                password='pabd',
                                host='localhost',
                                port=5432)
        cursor=conexao.cursor()
        codigosql="SELECT * FROM usuario WHERE nome='"+nome+"';"
        cursor.execute(codigosql)

        result=cursor.fetchone()
        conexao.commit()
        conexao.close ()

        if result != None:
            nome= result [0]
            senha= result [1]
            codigo= result [2]
            usuario= Usuario(nome,senha,codigo)
        else:
            usuario=None
        return usuario                                                                                                                                                  