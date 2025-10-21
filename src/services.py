from connection import get_connect
from passlib.hash import pbkdf2_sha256 as sha256

def criar_usuario(nome, email, senha):
    try:
        conn = get_connect()
        cursor= conn.cursor()
        cursor.execute('INSERT INTO TB_USUARIO_SAMUEL_R(nome, email, senha) VALUES(?,?,?)', 
                       (nome, email, senha))
        
        conn.commit()
        print('Usuário cadastrado com sucesso!')
    
    except Exception as e:
        print(f'Falha ao criar tabela: {e}')
    
    finally:
        
        cursor.close()
        conn.close()        


def listar_usuario():
    try:
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute('SELECT NOME, EMAIL, SENHA FROM TB_USUARIO_SAMUEL_R')
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
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute(""" 
DELETE FROM TB_USUARIO_SAMUEL_R WHERE ID=?
""", (id,))
        
        conn.commit()

    except Exception as e:
        print(f'Falha ao criar usuário: {e}')

def editar_usuario(id, novo_nome=None):
    try:
        conn = get_connect()
        cursor = conn.cursor()

        cursor. execute('SELECT * FROM TB_USUARIO_SAMUEL_R WHERE ID=?',(id,))
        usuario = cursor.fetchone()
        if not usuario:
            print('Usuário não encontrado')
            return
        campos =[]
        valores = []
        if novo_nome:
            campos.append('NOME=?')
            valores.append(novo_nome)
    except Exception as e:
        print('Falha ao editar usuário {e}')

def listar_usuario_email(id):
    ...

def listar_usuario_id(email):
    ...

def criar_tabela():
    try:
        conn = get_connect()
        cursor= conn.cursor()
        cursor.execute('''
        CREATE TABLE TB_USUARIO_SAMUEL_R(
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

#tabela produto
def cadastrar_Produto(Dscr, Qnt, Prc):
    try:
        conn = get_connect()
        cursor= conn.cursor()
        cursor.execute('INSERT INTO TB_USUARIO_SAMUEL_R(Dscr, Qnt, Prc) VALUES(?,?,?)', 
                       {Dscr},{Qnt},{Prc})
        
        conn.commit()
        print('Produto cadastrado com sucesso!')
    
    except Exception as e:
        print(f'Falha ao criar tabela de produtos: {e}')
    
    finally:
        
        cursor.close()
        conn.close()        


def listar_produtos():
    try:
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute('SELECT , EMAIL, SENHA FROM TB_USUARIO_SAMUEL_R')
        usuarios = cursor.fetchall()
        if usuarios:
            print(f'{30*'-'}Lista de usuários! {30*'-'}')
            for u in usuarios:
                print(f'|{u}')
        else:
            print('Nenhum usuário encontrado!')
    except Exception as e:
        print(f'Falha ao criar a lista {e}')

def vender_usuario(id):
    try:
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute(""" 
DELETE FROM TB_USUARIO_SAMUEL_R WHERE ID=?
""", (id,))
        
        conn.commit()

    except Exception as e:
        print(f'Falha ao criar usuário: {e}')
    '''
    id, quantidade saída) vender
    gtd_restante= gtd banco - gtd-saída
    if gtd banco > 0
    if gtd-banco>gtd-said
    '''

def editar_usuario(id):
    ...

def listar_usuario_email(id):
    ...

def listar_usuario_id(email):
    ...

def criar_tabela():
    try:
        conn = get_connect()
        cursor= conn.cursor()
        cursor.execute('''
        CREATE TABLE TB_USUARIO_SAMUEL_R(
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255) 
         );
''')
    except:
        ...
