'''
import mysql.connector
def get_connect():
    
    return mysql.connector.connect(
            host= '195.179.238.1',
            user= 'u275872813_2ds',
            password='Controlegasto25',
            database= 'u275872813_controle_gasto'
        )
com = get_connect()
cursor =...
'''
import sqlite3
def get_connect():
    try:
        conexao = sqlite3.connect('controle_usuario.db')
        print('Conexão bem sucedida!')
        return conexao
    
    except sqlite3.Error as e:
        print('Falha na conexão', e)
        return None
    
if __name__ == '__main__':
    get_connect()