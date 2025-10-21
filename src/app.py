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