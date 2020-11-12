#This file will highlight the main points when creating and persisting objects to the database

#Importing necessary attributes from sqlalchemy
from sqlalchemy import create_engine, MetaData , Table, Integer, String , Column, DateTime , ForeignKey, Numeric, Date , SmallInteger , PrimaryKeyConstraint , UniqueConstraint
#Importing the vase calss from sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
#Importing datetime to use for time related attributes
from datetime import datetime
#importing reltionship
from sqlalchemy.orm import relationship

#importing Session
from sqlalchemy.orm import Session



#Must indicate the type of database and driver in the connection string
engine = create_engine('mysql+mysqlconnector://root:root@localhost/python_practice' , echo =True)

#Initilise base class
Base = declarative_base()


#creating the customer class and it's mapping
class Customer(Base):
    #Class must always have a table name attribute to map it to the database
    __tablename__ = "customers"
    id = Column(Integer, primary_key = True)

    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)


#creates the table
def createTable():
    Base.metadata.create_all(engine)


"""
When using SQLAlchemy ORM, we interact with the database using the Session object

The Session object also wraps the database connection and transaction.
The transaction implicitly starts as soon as the Session starts communicating 
with the database and will remain open until the Session is committed, rolled back or closed.

To create a session you must use the Session class from the sqlalchemy.orm package 
You must creatre a session object everytime you want to communicate to the database

"""

#Session is created and you must set the bind parameter to the engine variable
session = Session(bind=engine)

#Note that instantiating Session object doesn't instantly establish connection to the database.
# The connection is established only when you start sending queries to the database.

#Inserting Data 

"""
To create a new records using orm we follow these steps
1. create an object
2. add the object to the session - this is esstentiially placing objects in a persisted state which then adds objects to the database upon the next flush/commit
3. commit the session - flushes all transactions to the database esstinally commmiting all transactions regardless of the state
"""

def addDB():
    #Objects created which match the schema
    c1 = Customer(name = 'Toby', 
                address = 'blanch', 
                email = 'tmiller@example.com', 
                
                )

    c2 = Customer(name = 'Roby', 
                address = 'tallaght', 
                email = 'robyt@example.com', 
                
                )

    #session.add() adds one object at a time
    #session.add_all() takes in a ist of objects and adds them in one go
    #the objects are now in a persisted state and ready to be inserted into the database
    session.add_all([c1, c2])
    #The session then commits it's transaction thus creating inserting the items
    session.commit()

if __name__ == "__main__":
    #createTable()
    addDB()