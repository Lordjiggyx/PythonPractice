#Connecting to a database

"""
To create a database in python you must import the create_engine class from sqlalchemy
An obejct of this class is created when using the create_engine() method 

this method takes the database as the argument

THE DATABASE MUST EXIST FIRST

To actually connect to the database you need the correct driver in this case iwant to use mysql so i needed the mysqlconnector driver this is the same for each different DB

"""

from sqlalchemy import create_engine ,Table , Column , Integer , String , MetaData, ForeignKey

#Must indicate the type of database and driver in the connection string
engine = create_engine('mysql+mysqlconnector://root:root@localhost/python_practice' , echo =True)
#USED TO CREATE DATABASE - Returns an object of type connection
engine.connect()

#The database connection object is returned
print(engine)