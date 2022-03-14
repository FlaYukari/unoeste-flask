# serve para persistir os dados de um cliente no banco de dados.
# classe responsavel por incluir o cliente no BD.

#As classes armazenadas na pasta Persistencia possuirão a responsabilidade de se comunicar com o banco de dados.
from Servidor.Modelo.Cliente import Cliente
import sqlite3

caminhoBancoDeDados = 'C:/Users/flayu/OneDrive/Curso/UNOESTE/2022-1 bimestre/internet/projetoweb/Servidor/Persistencia/dados/BancoDeDados.db'

class ClienteBD(object):

    def __init__(self):
        self.__conexao = sqlite3.connect(caminhoBancoDeDados)
        with self.__conexao as con:
            con.execute("""
            CREATE TABLE IF NOT EXISTS Cliente(
                codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                rg TEXT NOT NULL,
                cpf TEXT NOT NULL,
                dataNasc TEXT NOT NULL,
                endereco TEXT NOT NULL,
                num TEXT NOT NULL,
                complemento TEXT NOT NULL,
                bairro TEXT NOT NULL,
                cep TEXT NOT NULL,
                cidade TEXT NOT NULL,
                uf TEXT NOT NULL,
                telFixo TEXT NOT NULL,
                telCel TEXT NOT NULL
            )
            """)
            con.commit()

    
    def incluir(self, cliente):
        if isinstance(cliente, Cliente):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    INSERT INTO Cliente(nome, rg, cpf, dataNasc, endereco, num, complemento, bairro, cep, cidade, uf, telFixo, telCel)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """, (cliente.nome, cliente.rg, cliente.cpf, cliente.dataNasc, cliente.endereco, cliente.num, cliente.complemento, cliente.bairro, cliente.cep, cliente.cidade, cliente.uf, cliente.telFixo, cliente.telCel))
                cliente.codigo = cursor.lastrowid
                con.commit()
            

    def alterar(self, cliente):
            if isinstance(cliente, Cliente):
                with self.__conexao as con:
                    cursor = con.cursos()
                    cursor.execute("""
                        UPDATE Cliente SET nome = ?, rg = ?, cpf = ?, dataNasc = ?, endereco = ?, num = ?, complemento = ?, bairro = ?, cep = ?, cidade = ?, uf = ?, telFixo = ?, telCel = ? WHERE  codigo = ?
                    """, (cliente.nome, cliente.rg, cliente.cpf, cliente.dataNasc, cliente.endereco, cliente.num, cliente.complemento, cliente.bairro, cliente.cep, cliente.cidade, cliente.uf, cliente.telFixo, cliente.telCel))
                    con.commit()

        
    def apagar(self, cliente):
        if isinstance(cliente, Cliente):
            with self.__conexa as con:
                cursor = con.cursos()
                cursor.execute("""
                    DELETE FROM Cliente WHERE codigo = ?
                """, [cliente.codigo])
                con.commit()


    def consultar(self, termo):
        if isinstance(termo, int):
            #consultando pelo código do Cliente
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    SELECT nome, rg, cpf, dataNasc, endereco, num, complemento, bairro, cep, cidade, uf, telFixo, telCel
                    WHERE codigo = ?
                """)
                resultado = cursor.fetchone()
                if resultado:
                    cliente = Cliente(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8], resultado[9], resultado[10], resultado[11], resultado[12])
                    return cliente
                else:
                    None
        elif isinstance(termo, str):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    SELECT nome, rg, cpf, dataNasc, endereco, num, complemento, bairro, cep, cidade, uf, telFixo, telCel FROM cliente
                    WHERE nome like ?
                """, ["%" + termo + "%"])
                resultados = cursor.fetchall()
                listaPets = []
                for resultado in resultados:
                    cliente = Cliente(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8], resultado[9], resultado[10], resultado[11], resultado[12])
                    listaPets.append(cliente)
                return listaPets
        else:
            return None
