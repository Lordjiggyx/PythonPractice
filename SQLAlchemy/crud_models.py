#This file is used to create the models using in crud.py 

#Importing necessary attributes from sqlalchemy
from sqlalchemy import create_engine, MetaData , Table, Integer, String , Column, DateTime , ForeignKey, Numeric, Date , SmallInteger , PrimaryKeyConstraint , UniqueConstraint
#Importing the vase calss from sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
#Importing datetime to use for time related attributes
from datetime import datetime
#importing the mapper function
from sqlalchemy.orm import mapper
#importing reltionship
from sqlalchemy.orm import relationship

#Initilise base class
Base = declarative_base()


#Must indicate the type of database and driver in the connection string
engine = create_engine('mysql+mysqlconnector://root:root@localhost/python_practice' , echo =True)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    #Order will have a attribute called customers
    orders = relationship("Order", backref='customer')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price =  Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2),  nullable=False)
    

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    #This is another way of creating an asscoaiation table by using a class
    #here we pass in the name of the class, then the name of the assocation table and then finally create an attribute in the Ordline model called orders
    line_items = relationship("OrderLine", secondary="order_lines", backref='order')
    
#This class is actually an assocation table
class OrderLine(Base):
    __tablename__ = 'order_lines'
    id =  Column(Integer(), primary_key=True)
    #Has both the order id and item id as attributes
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    #Also has item as one to many relationship in the Item model there will now be an items attribute
    item = relationship("Item")

#Models are added to the database
Base.metadata.create_all(engine)