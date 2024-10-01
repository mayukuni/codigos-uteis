from bson.objectid import ObjectId
from typing import Dict, List


class testeRespository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "teste"
        self.__db_connection = db_connection

    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document

    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents

    def select_many(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        objetos = collection.find(
            filter,  # o que eu quero que busque
            {"_id": 0}  # filtro de chaves de valores que vão aparecer, 0 é false e 1 é true
        )

        response = []
        for objeto in objetos:
            response.append(objeto)
        return response

    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter, {"_id": 0})
        return response

    def select_if_property_exists(self, filter) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        objetos = collection.find(filter, {"_id": 0})
        response = []
        for objeto in objetos:
            response.append(objeto)
        return response

    def select_many_order(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        objetos = collection.find(
            filter,  # o que eu quero que busque
            {"_id": 0}  # filtro de chaves de valores que vão aparecer, 0 é false e 1 é true
        ).sort([("idade", 1)])  # ordena pelo valor da idade, -1 é decrescente e 1 é crescente

        response = []
        for objeto in objetos:
            response.append(objeto)
        return response

    def select_or(self, filter) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        objetos = collection.find(filter, {"_id": 0})
        response = []
        for objeto in objetos:
            response.append(objeto)
        return response
    
    def select_by_object_id(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        objetos = collection.find({"_id": ObjectId("66fc07aed23912c13056b50c")})
        response = []
        for objeto in objetos:
            response.append(objeto)
        return response
