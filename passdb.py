from pymongo import MongoClient


class Db():


    def __init__(self): #Makes Connection To DB


        client = MongoClient('mongodb://localhost:27017/')

        db= client ['pass-database']
        self.record= db.record




    def lookup(self,request): #Bring up records based on user
           users = self.record.find({'username': request})
           services = self.record.find({'service': request})
           for datarecord in users:
               print datarecord['password'] + " for service account " + datarecord['service']

           for datarecord in services:
               print datarecord['password'] + " owner of "  + datarecord['username']




    def record_insert(self,**args): #Insert records entered into DB

        records = self.record.insert(args)

        return records

    def delete_all(self,**args):  #Clears Entire DB

        del_records = self.record.delete_many({})

        return  del_records

#THINK OF MORE FUCNTIONALITY FOR LOOKUPS AND SERVICES





