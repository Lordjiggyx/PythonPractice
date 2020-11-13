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
engine = create_engine('mysql+mysqlconnector://root:root@localhost/python_practice')

#Initilise base class
Base = declarative_base()

#This command will stop the logging
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

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


#Querying database

"""
all select statemets are created by a query object

to create a query object it follows this format

query = session.query(mapped class)

this is the same as the follwoing 
query = Query(mapped clas , session)

The query object has all() method which returns a resultset in the form of a list of objects 


USEFUL METHODS USED IN QUERY OBJECT

1	add_columns()
It adds one or more column expressions to the list of result columns to be returned.

2	
add_entity()

It adds a mapped entity to the list of result columns to be returned.

3	
count()

It returns a count of rows this Query would return.

4	
delete()

It performs a bulk delete query. Deletes rows matched by this query from the database.

5	
distinct()

It applies a DISTINCT clause to the query and return the newly resulting Query.

6	
filter()

It applies the given filtering criterion to a copy of this Query, using SQL expressions.

7	
first()

It returns the first result of this Query or None if the result doesn’t contain any row.

8	
get()

It returns an instance based on the given primary key identifier providing direct access to the identity map of the owning Session.

9	
group_by()

It applies one or more GROUP BY criterion to the query and return the newly resulting Query

10	
join()

It creates a SQL JOIN against this Query object’s criterion and apply generatively, returning the newly resulting Query.

11	
one()

It returns exactly one result or raise an exception.

12	
order_by()

It applies one or more ORDER BY criterion to the query and returns the newly resulting Query.

13	
update()

It performs a bulk update query and updates rows matched by this query in the database.
""" 

def queryDB():
    #its best to assign the result set to a variable 
    result = session.query(Customer).all()
    #Print all values in the resultset with a loop
    # here you can pull the attributes from the db and display them
    for row in result:
        print("Name of User:",row.name)

#Updating DB 

"""
To update any attribute of an object we have to assign a new value to it and ocmmit the chanages to make the chane persisent

literally you grab the object and then assgin the new value and commit

To do a bul update we use the update() method from the query object 
this method needs two parameters 
1. a dictionary of key-value with the key being the attribure to be updated and the vale being the new content
2. synchronize_session - this is the strategy to update attributes in the session there are 3 valid valued
    False- does not sync the session
    Fetch - does a aswlwct query before the update to find ojects that are matched by the update query
    Evaluate - evaluate criteria on objects in the session
"""

def updateDB(changename):
    #Querying first object
    first = session.query(Customer).get(1)
    #Print the name 
    print(first.name)

    #change the name to match whatever is passed into the method
    first.name = changename
    #commit to db
    session.commit()

    #check change was made
    check = session.query(Customer).get(1)
    print(check.name)


def bulkUpdate():
    #Using the query to get the result set of customers
    #then calling the update method
    session.query(Customer).update(
    {
    Customer.name: "Corrected",
    Customer.address:"Changed"
    },
    synchronize_session= False
    )
    #finally commit it
    session.commit()
    print("done")

#Filtering

"""
To filter in sqlalchemy you can use the filter method that the query object has
the method follows the general form

session.query(class).filter(creiteria)

there are mutiple filter operators

== - this operator is used fo a check of equality
!= this operator is used to determine non equality
like() - this method produces the LIKE criteria for the Where clause in a select expression mostly used for regex filterinhg
in_() - This operator checks whetter the column value belongs to a collection of items in a list
and_() ,- These operators are used to concatenate multiple criteria which mut match you can actually use & but weach condtion must be in brackets
or_() - This operator is used to provide concatenate multiple criteria which may not all match you can actually use |s but weach condtion must be in brackets

"""

def fileterDB():
    #filter to get any object with an id greater than 1
    greaterThan2 =session.query(Customer).filter(Customer.id>1)
    
    for x in greaterThan2:
        print(x.name)

def filerOperators():
    x = "*" *20

    print(x)
    print("EQUALS")
    result = session.query(Customer).filter(Customer.id == 1)
    
    for row in result:
        print("Name is:",row.name)
   
    print(x)

    print(x)
    print("NOT EQUALS")
    result = session.query(Customer).filter(Customer.id != 1)
    
    for row in result:
        print("Name is:",row.name)
   
    print(x)

    print(x)
    print("LIKE")
    result = session.query(Customer).filter(Customer.name.like("T%"))
    
    for row in result:
        print("Name is:",row.name)
   
    print(x)

    print(x)
    print("IN")
    result = session.query(Customer).filter(Customer.id.in_({1,4}))
    
    for row in result:
        print("Name is:",row.name)
   
    print(x)

    print(x)
    print("AND")
    result = session.query(Customer).filter((Customer.id>1) & (Customer.name.like("T%")) )
    
    for row in result:
        print("Name is:",row.name)
   
    print(x)

    print(x)
    print("OR")
    result = session.query(Customer).filter((Customer.id>1) | (Customer.name.like("T%")) )
    
    for row in result:
        print("Name is:",row.name)
   
    print(x)

if __name__ == "__main__":
    #Run methods as you see fit 
    #createTable()
    #addDB()
    #queryDB()
    #updateDB("Tim")
    #ulkUpdate()
    filerOperators()
    # fileterDB()