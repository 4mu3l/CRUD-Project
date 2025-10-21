#Mercado precisa de de duas tabelas, usuário e produto
#Na tabela produto precisa de id, descrição, quantidade e preço
#tabela usuário precisa de um id, email, sennha e nome

#as duas tabelas precisam cadastrar e listar 
#na tabela usuário precisa ter cadastrar e fazer login se tiver conta
#tabela produto, esse produto precisa ser vendido 

#importações
from connection import get_connect
from passlib.hash import pbkdf2_sha256 as sha256

#Criar usuário
def criar_usuario(nome, email, senha):
    try:
        conn = get_connect()
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

#Lista de usuário

def listar_usuario():
    try:
        conn = get_connect()
        cursor = conn.cursor()
        cursor.execute('SELECT NOME, EMAIL, SENHA FROM TB_USUARIO')
        usuarios = cursor.fetchall()
        if usuarios:
            print(f'{30*'-'}Lista de usuários! {30*'-'}')
            for u in usuarios:
                print(f'|{u}')
        else:
            print('Nenhum usuário encontrado!')
    except Exception as e:
        print(f'Falha ao criar a lista {e}')

def criar_tabela():
    try:
        conn = get_connect()
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


