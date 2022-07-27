import pymongo

client = pymongo.MongoClient("mongodb+srv://mongodb:New12345@cluster0.wfbiibu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d ={
    "name": 'raunak',
    'email': 'r@gmail.com',
    'surname' : 'ravi'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

d1 ={
    "name": 'raunak',
    'email': 'r@gmail.com',
    'surname' : 'ravi'
}