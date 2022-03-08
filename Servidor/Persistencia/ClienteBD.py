# serve para persistir os dados de um cliente no banco de dados.
# classe responsavel por incluir o cliente no BD.

#As classes armazenadas na pasta Persistencia possuirão a responsabilidade de se comunicar com o banco de dados.
from Modelo.Cliente import Cliente
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
            
