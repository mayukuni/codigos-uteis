from models.connection_options.connection import DBConnectionHandler
from models.repository.teste_repository import testeRespository

db_handle = DBConnectionHandler()
# conn1 = db_handle.get_db_connection()
# print(conn1)

db_handle.connect_db()
db_connection = db_handle.get_db_connection()

teste_repository = testeRespository(db_connection)

exemplo = {
    "nome": "vocee"
}

teste_repository.insert_document(exemplo)

lista_exemplo = [
    {"nome": "vocee"},
    {"nome": "tu"},
    {"nome": "ele"},
    {"nome": "aaa"},
]

teste_repository.insert_list_of_documents(lista_exemplo)
