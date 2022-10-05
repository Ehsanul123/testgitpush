import pymongo
client = pymongo.MongoClient("mongodb+srv://Ehsanul:Rat12345@cluster0.xe9xm.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d={
    "name":"Tom",
    "surname":"Gautam",
    "email_id":"tom@maximaapparel.com"
}

db1=client['mongootest']
coll=db1['test12']
coll.insert_one(d )