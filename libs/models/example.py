from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Define the database engine
# This connects to an in-memory SQLite database for simplicity.
# For other databases, you would adjust the connection string (e.g., 'postgresql://user:password@host:port/dbname').
engine = create_engine('sqlite:///:memory:', echo=True)

# 2. Define the Base class for declarative models
Base = declarative_base()

# 3. Define a table as a Python class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

# 4. Create the tables in the database
Base.metadata.create_all(engine)

# 5. Create a Session factory
Session = sessionmaker(bind=engine)
session = Session()

# 6. Add new data
user1 = User(name='Alice', email='alice@example.com')
user2 = User(name='Bob', email='bob@example.com')

session.add(user1)
session.add(user2)
session.commit() # Commit the changes to the database

# 7. Query data
# Get all users
all_users = session.query(User).all()
print("All users:", all_users)

# Get a user by name
alice = session.query(User).filter_by(name='Alice').first()
print("Alice:", alice)

# Get users with a specific email domain
example_users = session.query(User).filter(User.email.like('%@example.com')).all()
print("Users with @example.com:", example_users)

# 8. Update data
if alice:
    alice.name = 'Alicia'
    session.commit()
    print("Updated Alice:", session.query(User).filter_by(id=alice.id).first())

# 9. Delete data
if user2:
    session.delete(user2)
    session.commit()
    print("Users after deleting Bob:", session.query(User).all())

# 10. Close the session
session.close()