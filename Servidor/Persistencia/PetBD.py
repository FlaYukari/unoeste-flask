# serve para persistir os dados de um pet no banco de dados.
# classe responsavel por incluir o pet no BD.

#As classes armazenadas na pasta Persistencia possuirão a responsabilidade de se comunicar com o banco de dados.
from Modelo.Pet import Pet
import sqlite3

caminhoBancoDeDados = 'C:/Users/flayu/OneDrive/Curso/UNOESTE/2022-1 bimestre/internet/projetoweb/Servidor/Persistencia/dados/BancoDeDados.db'

class PetBD(object):

    def __init__(self):
        self.__conexao = sqlite3.connect(caminhoBancoDeDados)
        with self.__conexao as con:
            con.execute("""
            CREATE TABLE IF NOT EXISTS Pet(
                codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                especie TEXT NOT NULL,
                raca TEXT NOT NULL,
                cor TEXT NOT NULL,
                dataNasc TEXT NOT NULL,
                numMicrochip TEXT NOT NULL,
                rga TEXT NOT NULL 
            )
            """)
            con.commit()

    
    def incluir(self, pet):
        if isinstance(pet, Pet):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    INSERT INTO Pet(nome, especie, raca, cor, dataNasc, numMicrochip, rga)
                    VALUES(?,?,?,?,?,?,?)
                """, (pet.nome, pet.especie, pet.raca, pet.cor, pet.dataNasc, pet.numMicrochip, pet.rga))
                pet.codigo = cursor.lastrowid
                con.commit()
            

    def alterar(self, pet):
        if isinstance(pet, Pet):
            with self.__conexao as con:
                cursor = con.cursos()
                cursor.execute("""
                    UPDATE Pet SET nome = ?, especie = ?, raca = ?, cor = ?, dataNasc = ?, numMicrochip = ?, rga = ? WHERE  codigo = ?
                """, (pet.nome, pet.especie, pet.raca, pet.cor, pet.dataNasc, pet.numMicrochip, pet.rga, pet.codigo ))