from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base




session = None

def get_session(engine):



    # 2. Define the Base class for declarative models
    Base = declarative_base()

    # 4. Create the tables in the database
    Base.metadata.create_all(engine)

    # 5. Create a Session factory
    Session = sessionmaker(bind=engine)
    session = Session()


    session.e