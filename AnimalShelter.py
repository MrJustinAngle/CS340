from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'Justin'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32290
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        try:
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
            self.database = self.client['%s' % (DB)]
            self.collection = self.database['%s' % (COL)]
            print("Connected")
        # prints the error if an error occurs while connecting
        except errors.ConnectionError as e:
            print(f'Could not connect to MongoDB: {e}')
    
    # defining the create function
    def create(self, data):
        print("in create method")
        # method to add new data to the database
        if data is not None:
            
            self.collection.insert_one(data)
            return True

        else:
            raise Exception("Nothing to save, because data parameter is empty")
                        
    def read(self, searchTerm):
        print("in read method")
        # method to read the data that is in the database
        if searchTerm is not None:
            print("Search is not null")
            documents = self.collection.find(searchTerm)
            return documents

        else:
            
            raise Exception("Nothing to find, because search parameter is empyty")
        
            
    # defining the update function
    def update(self, searchTerm, infoChange):
        print("in update method")
        updatedAnimalsNum = 0 # to keep track of the number of animals updated
        
        if searchTerm and infoChange is not None: # if both are not blank it will run this
            resultSearch = self.collection.find(searchTerm) # creates a list of the results
            for animals in resultSearch: # a for loop to iterate through the results
                self.collection.update(searchTerm, infoChange) # changes each of the results
                updatedAnimalsNum += 1 # to keep track of number updated
        
        else:
            raise Exception("Nothing to update, as one of the fields were left blank.")
        
        # print number of updated animals
        print(f"Number of updated entries: {updatedAnimalsNum}")
        
    # defining the delete function
    def delete (self, searchTerm): 
        print("in delete method")
        deletedAnimalsNum = 0 # to keep track of number of animals deleted
        
        if searchTerm is not None: # if search term is not blank it will run this
            resultSearch = self.collection.find(searchTerm) # creates a list of the results
            for animals in resultSearch: # a for loop to iterate through the results
                self.collection.delete_one(searchTerm) # deletes the records with the searchterm
                deletedAnimalsNum += 1 # keeps track of the number of animals deleted
                
        else:
            raise Exception("Nothing to delete, as the field is empty.")
            
        print(f"Number of deleted entries: {deletedAnimalsNum}")
            
        
