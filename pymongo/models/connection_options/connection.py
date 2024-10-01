from pymongo import MongoClient
from .mongo_configs import infos


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = 'mongodb://{}:{}'.format(
            infos["HOST"],
            infos["PORT"]
        )
        self.__database_name = infos["DB_NAME"]

        self.__client = None
        self.__db_connection = None

    def connect_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]

    def get_db_connection(self):
        return self.__db_connection

    def get_db_client(self):
        return self.__client
