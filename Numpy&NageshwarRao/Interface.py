from abc import *

class DB:

    def connect(self):
        pass

    def disconnect(self):
        pass

class Oracle(DB):

    def connect(self):
        print("Connecting to Oracle database")

    def disconnect(self):
         print("Disconnecting from Oracle database")

class Sybase(DB):

    def connect(self):
        print("Connecting to Sybase database")

    def disconnect(self):
         print("Disconnecting from Sybase database")
    
str = input("Please enter the DB name")

classname = globals()[str]

o = classname()
o.connect()
o.disconnect()

print("--------------------------------------------------")

str = input("Please enter the DB name")

classname = globals()[str]

s = classname()
s.connect()
s.disconnect()
