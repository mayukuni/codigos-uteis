from models.connection_options.connection import DBConnectionHandler
from models.repository.teste_repository import testeRespository

db_handle = DBConnectionHandler()
# conn1 = db_handle.get_db_connection()
# print(conn1)

db_handle.connect_db()
db_connection = db_handle.get_db_connection()

teste_repository = testeRespository(db_connection)

exemplo = {
    "nome": "vocee",
    "idade": "6"
}

# teste_repository.insert_document(exemplo)

lista_exemplo = [
    {"nome": "vocee"},
    {"nome": "tu",
     "idade": "2"},
    {"nome": "ele"},
    {"nome": "aaa",
     "cores": {
         "azul": 1,
         "rosa": "3"
     }},
]

# teste_repository.insert_list_of_documents(lista_exemplo)

result = teste_repository.select_many({"nome": "vocee"})
print(result)

result2 = teste_repository.select_one({"nome": "vocee"})
# print(result2)

result3 = teste_repository.select_if_property_exists({"idade": {"$exists": True}})
# print(result3)

result4 = teste_repository.select_many_order({"nome": "vocee"})
print()
print(result4)

result5 = teste_repository.select_or({"$or": [{"nome": "tu"}, {"idade": {"$exists": True}}]})
print("vaaa", result5)

result6 = teste_repository.select_by_object_id()
print("ultimo", result6)
