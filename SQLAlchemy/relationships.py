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


"""

Many To One
To create a Many to one relationship we place a foreighn key refering to the child class in the parent class
then relationship is declareed which holds the name of the child table
To make it bidrectional you add a backref valiue in each class refering to both calsses
"""


def createManyToOne():

    class MT0Parent(Base):
        __tablename__ = "MTOParent"
        id = Column(Integer, primary_key = True)
        #Foreign key of child
        child_id = Column(Integer, ForeignKey("MTOChild.id"))
        #bidretional reference is made
        children = relationship("MTOPChild" , backref="parents")

    class MT0Child(Base):
        __tablename__ = "MTOChild"
        id = Column(Integer, primary_key = True)
        #bidretional reference is made
        child = relationship("MTOParent" , backref="children")

    Base.metadata.create_all(engine)

"""
One To One
To create a one to one relationship we place a foreighn key refering to the parent class in the child class
then relationship is declareed which holds the name of the child table and uselist is passed in and set to false and then backref

in the child calss you make it bidrectional by making a relationship and refernecing the parent table and relationship value

"""


def createOneToOne():

    class OneToOneParent(Base):
        __tablename__ = "OTOParent"
        id = Column(Integer, primary_key = True)
        #realtionship is made and uselist is set to false  reference is made
        child = relationship("OTOChild" ,uselist=False, backref="parent")
        
    class OneToOneChild(Base):
        __tablename__ = "OTOChild"
        id = Column(Integer, primary_key = True)
        #foreign key to parent is made
        parent_id =  Column(Integer, ForeignKey("OTOParent.id"))
        #realtionship is made and uselist is set to false  reference is made
        children = relationship("OTOParenr" , backref="child")
    
    Base.metadata.create_all(engine)



"""
Mnay To Many

Probably the best way to make a many to many object is to use an asscociation object, this is beacuse this table may one day need extra info apart from foreign keys

SO create a left and right id in this object
even though it is a many to many relationship there is stoill some sort of parent child relationship 

To make the assocatiation table bi directional it must have a relationship to both the parent and the child classes 
and the parent and child must both refernce the assocatiation object and make reference to the assoctaion tables values that refers to both parent and child

"""

def createManyToMany():
    class Association(Base):
        __tablename__ = 'association'
        left_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
        right_id = Column(Integer, ForeignKey('right.id'), primary_key=True)
        extra_data = Column(String(50))
        #reference to both parent and child
        child = relationship("Child", back_populates="parents")
        parent = relationship("Parent", back_populates="children")

    class Parent(Base):
        __tablename__ = 'left'
        id = Column(Integer, primary_key=True)
        #reference to parent
        children = relationship("Association", back_populates="parent")

    class Child(Base):
        __tablename__ = 'right'
        id = Column(Integer, primary_key=True)
        #reference to parent
        parents = relationship("Association", back_populates="child")
    
    # create parent, append a child via association
    p = Parent()
    a = Association(extra_data="some data")
    a.child = Child()
    p.children.append(a)

    # iterate through child objects via association, including association
    # attributes
    for assoc in p.children:
        print(assoc.extra_data)
        print(assoc.child)

        Base.metadata.create_all(engine)


"""
working with this pattern means that child objects must be associated with an assocatiaon object instance before being appended to the parent 
and access from parent to child goes through the associatio object


"""

if __name__ == "__main__":
    #Run methods as you see fit 
    #createOneToMany()
    # createManyToOne()
    #createOneToOne()
    createManyToMany()
    