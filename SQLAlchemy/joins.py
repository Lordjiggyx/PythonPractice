#Joins

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
engine = create_engine('mysql+mysqlconnector://root:root@localhost/relationshippractice')

#Initilise base class
Base = declarative_base()

#Session is created and you must set the bind parameter to the engine variable
session = Session(bind=engine)

class Customer(Base):
    #Class must always have a table name attribute to map it to the database
    __tablename__ = "customer"
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key = True)
    #fOREIGN KEY ESTABLISHED
    custID = Column(Integer, ForeignKey("customer.id"))
    address = Column(Integer)
    amount = Column(Integer)
    # establishing bidirectional relationship
    customer = relationship("Customer" , backref="invoices")

"""
Joins allow us to query multiple tables at the same time

To create an implicit join we can use the query.filter() method to equate the related columns together

The actual join commmand in ssql is achived using the .join() method 
you query one table and call the join method while passing in the other table 
"""

#Implicit Join

def implicit():
    #This gets both the customer and invoice objects from the databases where the ID's match
    for c,i in session.query(Customer, Invoice).filter(Customer.id == Invoice.custID).all():
        print("ID: {} Name: {} Amount: {}".format(c.id,c.name,i.amount))


def join():
    #a proper join is called and we retrive all the details from  both tables where the invoice amount is 8500
    result = session.query(Customer).join(Invoice).filter(Invoice.amount>8500).all()

    #To get information from this result set we just iterate through it using a for loop
    for row in result:
        for inv in row.invoices:
            print(row.name, inv.amount)


if __name__ == "__main__":
    #implicit()
    join()
