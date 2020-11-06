#Defining schemas in SQLAlchemy ORM

"""
The SQLAlchemy ORM is a way to define tables and realtionships between them using python classes
It also provides a way to query and manipulate the database using object orientated code
"""


#Defining Models
"""
A Model is a Python class which corresponds to the database table and its attributes represent the columns.

For the class to be a valid model, it must do the following:

***Inherit from a declarative base class created by calling declarative_base() function.****
define table name via __tablename__ attribute.
define at-least one column which must be a part of the primary key.

The base class maintains a catalog of classes and tables, this calss wraps the mapper and the metadata
The mapper maps the subclass to the table and metadata hold the information about the databases and the tables it contains
"""

#THIS EXMPLE WILL CREATE A POST MODEL THAT WILL BE USED TO STORE BLOG POSTS

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

#Create the Post class pass in base class and then create the attributes
class Post(Base):
    #Assigning a name to the table
    __tablename__="Posts"
    #<Variable_Name> = Column(<column_type>, addtional args)
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    Content = Column(String(100), nullable=False)
    Author = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default = datetime.now)
    updated_on = Column(DateTime, default = datetime.now, onupdate=datetime.now)



#Adding Keys and constraints 
"""
When adding keys and constraints in ORM we use the __table_args__ atribute this goes underneath the class attributes
"""

class User(Base):
    __tablename__ = "users"
    id = Column(Integer)
    name = Column(String(100), nullable=False)
    eamil = Column(String(100), nullable=False)
    
    __table_args__ = (
        PrimaryKeyConstraint("id" , name = "user_pk"),
        UniqueConstraint('username'),
        UniqueConstraint('email'),
    )



#Defining Relationships

#One to Many

"""To create a one to many relationship we place a foreign key on the child class"""

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    #The relationship fnuctions adds attributes on the models to access the related data
    #This line essentially adds a books attribute to the author class so we can access the books using Author.books
    books = relationship("Book")

class Book(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)
    #This line esavlishes a relationship between the author and book model
    author_id = Column(Integer, ForeignKey('authors.id'))
    #To make the relationship bidirectional you can define a relationship in the child class related to the parent
    #Now Book can access it's author using b.author
    author = relationship("Author")


#One to One 

"""
Establishing a one-to-one relationship in SQLAlchemy is almost the same as one-to-many relationship,
the only difference is that we pass an additional argument ****uselist=False**** to the relationship() function. 
"""

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    designation = Column(String(255), nullable=False)
    doj = Column(Date(), nullable=False)
    #BACKREF CAN BE USED TO ADD A VARIBALE RELATING TO THE PARENT/CHILD ON THE OTHER END
    #THIS MEANS DRIVERLICENSE WILL HAVE AN ATTRIBUTE .person
    dl = relationship('DriverLicense', backref='person', uselist=False)

class DriverLicense(Base):
    __tablename__ = 'driverlicense'
    id = Column(Integer(), primary_key=True)
    license_number = Column(String(255), nullable=False)
    renewed_on = Column(Date(), nullable=False)
    expiry_date = Column(Date(), nullable=False)
    person_id = Column(Integer(), ForeignKey('persons.id'))  # Foreign key


#Many to Many

"""
Creating a many-to-many relationship requires an extra table called an association table or an intermediary table.
 We define this table as an instance of the Table class and then connect it to the model using the ****secondary*** argument of the relationship() function.
"""

#This is the assoctaion table you give it a name and pass in Base.metadata to store information on it 
#Then you idnetify the columns with both identifying keys 
author_book = Table('author_book', Base.metadata, 
    Column('author_id', Integer(), ForeignKey("authors.id")),
    Column('book_id', Integer(), ForeignKey("books.id"))
)

class Author1(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

class Book1(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    #We pass in the author book(the associataion table) as a varible for the secondary attribute
    author = relationship("Author", secondary=author_book, backref="books")

"""
So now you can usek Author.books to get a list of books writeen by a specfic author
And vice versa you can use Book.Authors which will retirn a list of author objects

"""

#To create tables you use the Base.metadata.create_all(engine)
#To drop  tables you use the Base.metadata.create_all(engine)