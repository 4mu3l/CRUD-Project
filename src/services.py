from connection import get_connection
from passlib.hash import pbkdf2_sha256 as sha256

def criar_usuario(nome, email, senha):
    try:
        conn = get_connection()
        cursor= conn.cursor()
        cursor.execute('INSERT INTO TB_USUARIO_SAMUEL_R(nome, email, senha) VALUES(?,?,?)', 
                       {nome},{email},{senha})
        
        conn.commit()
        print('Usuário cadastrado com sucesso!')
    
    except Exception as e:
        print(f'Falha ao criar tabela: {e}')
    
    finally:
        
        cursor.close()
        conn.close()        


def listar_usuario():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT NOME, EMAIL SENHA FROM TB_USUARIO')
        usuarios = cursor.fetchall()
        if usuarios:
            print(f'{30*'-'}Lista de usuários! {30*'-'}')
            for u in usuarios:
                print(f'|{u}')
        else:
            print('Nenhum usuário encontrado!')
    except Exception as e:
        print(f'Falha ao criar a lista {e}')

def excluir_usuario(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(""" 
DELETE FROM TB_USUARIO WHERE ID=?
""", (id,))
        
        conn.commit()

    except Exception as e:
        print(f'Falha ao criar usuário: {e}')

def editar_usuario(id):
    ...

def listar_usuario_email(id):
    ...

def listar_usuario_id(email):
    ...

def criar_tabela(id):
    try:
        conn = get_connection()
        cursor= conn.cursor()
        cursor.execute('''
        CREATE TABLE TB_USUARIO(
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255) 
         );
''')

    except Exception as e:
        print(f'Falha ao criar tabela: {e}')

if __name__ == '__main__':
    criar_tabela()
    nome=input('Digite um nome: ').strip().title()
    email=input('Digite um email: ').strip()
    senha=input('Digite uma senha: ').strip()
    senha = sha256.hash(senha)
    print(senha)
    criar_usuario(nome,email,senha)
    listar_usuario()