import sqlite3
from sqlite3 import Connection

class DbConnectionHandler:
    def __init__(self) -> None:
        self .__connection_string = "storage.db" # Caminho para o banco de dados SQLite
        self .__conn = None # Armazenamento da conexão com o banco

    def connect(self) -> None:
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        self.__conn = conn

    def get_connection(self) -> Connection:
        return self.__conn
    
# Objeto para garantir uma única conexão
db_connection_handler = DbConnectionHandler()