#Crud functionality using ORM

"""
When using SQLAlchemy ORM, we interact with the database using the Session object
The Session object also wraps the database connection and transaction.
The transaction implicitly starts as soon as the Session starts communicating 
with the database and will remain open until the Session is committed, rolled back or closed.

To create a session you must use the Session class from the sqlalchemy.orm package 

You must creatre a session object everytime you want to communicate to the database

To do this SQLAlchemy provides sessionmaker class which creates Session class with default arguments set for its constructor.

You should call call sessionmaker once in your application at the global scope.

and from that you can instanstaite a session object as many times as you want
"""

#importing sqlalchemy and the neccessary attributes
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


#Import classes
from crud_models import Customer


#Must indicate the type of database and driver in the connection string
engine = create_engine('mysql+mysqlconnector://root:root@localhost/python_practice' , echo =True)

session = Session(bind=engine)

#Note that instantiating Session object doesn't instantly establish connection to the database.
# The connection is established only when you start sending queries to the database.



#Inserting Data 

"""
To create a new recors using orm we follow these steps

1. create an object
2. add the object to the session
3. commit the session
"""

c1 = Customer(first_name = 'Toby', 
              last_name = 'Miller', 
              username = 'tmiller', 
              email = 'tmiller@example.com', 
             
             )

c2 = Customer(first_name = 'Scott', 
              last_name = 'Harvey', 
              username = 'scottharvey', 
              email = 'scottharvey@example.com', 
             
             )

session.add_all([c1])
session.commit()