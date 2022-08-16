from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def init(self, username, password):
        self.client = MongoClient('mongodb://%s:%s@localhost:35359' % (aacuser2, g))
        self.database = self.client['AAC']
        
#create the method to implemement the C in CRUD
def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary 
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")  
            
#create method to implement the R in CRUD 
def read(self, data):
        return self.database.animals.find_one(data) ## returns only one document as a python dictionary
            
#Create method to implement the U in CRUD

def update(self, search):
        if search:
            result = self.database.animals.update_one(search,newValue)
            return result
        else:
            raise Exception("Document not found")
#Create method to implement the D in CRUD
def delete(self, search):
        if search:
            self.database.animals.delete_one(search)
            return True
        else:
            raise Exception("Document not found")
            
