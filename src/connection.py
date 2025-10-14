import mysql
import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conexao=mysql.connector.connect(
            host= '195.179.238.1',
            user= 'u275872813_2ds',
            password='Controlegasto25',
            database= 'u275872813_controle_gasto'
        )

        if conexao.is_connected():
            print('Conexão com o banco bem sucedida!')
            return conexao
    except Error as e:
        print('Falha ao conectar com o Banco!',e)
        return None
if __name__ == '__main__':
    get_connection()