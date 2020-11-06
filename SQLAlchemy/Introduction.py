"""
SQLAlchemy is an ORM written in python, it is like using mongoos for mongodb in JS, it's handy to use so i dont have to write sql in python code
It actually follows quite closely to hibernate but is pythonic

To start use the command pip install sqlalchemy and then import it 

SQLAlchemy by default only works with SQLite databases without any other drivers to work with other databases you need to insatl the corretc driver

There are 2 ways to use SQLAlchemy either use the ORM or Core, using Core is closer to SQL then ORM

Im gonna use ORM makes more sense and is easier to understand
"""
import sqlalchemy

"Checking the version"
print(sqlalchemy.__version__)