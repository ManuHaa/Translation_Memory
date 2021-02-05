
import os
import json
import uuid

uuids = []
basePath = os.path.dirname(os.path.abspath(__file__))


def getDBPath(dbName: str):
    if dbName == "general":
        return basePath + "/database/generalDB.json"
    elif dbName == "languages":
        return basePath + "/database/languagesDB.json"
    elif dbName == "registered":
        return basePath + "/database/registeredUsersDB.json"
    else:
        return basePath + "/database/policiesDB.json"


#-returns already generated 
def get_used_uuids() -> list:
    return uuids

#-adds an id to uuid storage
def add_uuid(id: str):
    get_used_uuids().append(id)

#-generates an individual uuid
def generate_uuid():
    id = str(uuid.uuid4())
    if id in get_used_uuids():
        return generate_uuid()
    add_uuid(id)
    return id

def getNumberOfAddedWords():
    dbFile = open(getDBPath("user"), "r")
    dbData = json.load(dbFile)
    dbFile.close()

    return dbData['addedWords']

def getNumberOfRegisteredWords():
    dbFile = open(getDBPath("words"), "r")
    dbData = json.load(dbFile)
    dbFile.close()
        
    return len(dbData['words'])

def getDBData(dbName):
    dbFile = open(getDBPath(dbName), "r")
    dbData = json.load(dbFile)
    dbFile.close()

    return dbData

def checkIfPairInDict(key, value, dictionary):
    if key in dictionary and value == dictionary[key]:
        return True
    else:
        return False

def killExec(state):
    state = False