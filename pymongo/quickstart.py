import pymongo   # noqa: F401
from pymongo import MongoClient

try:
    uri = "mongodb://localhost:27017"
    client = MongoClient(uri)

    database = client["teste"]
    # print(database)
    collection = database["teste"]

    print(collection)

    chave = {"Situação": "Situação: CANCELADA"}

    # achar dados
    items = collection.find(chave)
    print(items)

    for item in items:
        print(item)

    # inserir documento
    collection.insert_one({"teste": "123"})

    # inserir chave
    collection.update_one(
        {},
        {"$set": {"statddaaaaaaaaaaudddus": "actiive"}},
    )

    collection.update_many(
        {},
        {"$set": {"statddaaaaaaaaaaudddus": "actiive"}},
    )

    # collection.delete_one(
    #     {}
    # )

    # collection.delete_many(
    #     {}
    # )

    # db.collection.updateMany(
    #     <filter>,
    #     <update>,
    #     {
    #         upsert: <boolean>,
    #         writeConcern: <document>,
    #         collation: <document>,
    #         arrayFilters: [ <filterdocument1>, ... ],
    #         hint:  <document|string>
    #     }
    # )

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
