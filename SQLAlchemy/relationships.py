#You already covered relationships in the schema.py but this is just a more ran through better explanied file about them

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
#This command will stop the logging
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

#Must indicate the type of database and driver in the connection string
engine = create_engine('mysql+mysqlconnector://root:root@localhost/prelationships')

#Initilise base class
Base = declarative_base()

#Session is created and you must set the bind parameter to the engine variable
session = Session(bind=engine)

"""
One to many

This is a parent child relationship to do this you often indicate the foreignkey variable in the child class and then create a relationship highlighting the name of the child class
it's not always needed but me personally i believe it is best to make everything bidrectional to do this use the back_ref attribute in the relationshp method

THE NAME USED IN BACKREF MUST MATCH THE NAME OF THE BIDERECTIONAL RELATIONSHIP VARIBALE IN THE CHILD/PARENT CLASS

"""




#creates the table
def createOneToMany():
    #creating the customer class and it's mapping
    class Customer(Base):
    #Class must always have a table name attribute to map it to the database
        __tablename__ = "customer"
        id = Column(Integer, primary_key = True)
        name = Column(String(100), nullable=False)
        address = Column(String(100), nullable=False)
        email = Column(String(100), nullable=False)
        # establishing bidirectional relationship
        invoices = relationship("Invoice" , backref="customer")

    class Invoice(Base):
        __tablename__ = "invoices"
        id = Column(Integer, primary_key = True)
        #fOREIGN KEY ESTABLISHED
        custID = Column(Integer, ForeignKey("customer.id"))
        address = Column(Integer)
        amount = Column(Integer)
        # establishing bidirectional relationship
        customer = relationship("Customer" , backref="invoices")
        
    Base.metadata.create_all(engine)



if __name__ == "__main__":
    #Run methods as you see fit 
    createOneToMany()
    