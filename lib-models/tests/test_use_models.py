from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib_models import models, Base

User = models.User
User2 = models.User2

# https://docs.astral.sh/uv/concepts/projects/init/#libraries
def test_user_models_main():
    # pool config??
    # https://docs.sqlalchemy.org/en/20/core/pooling.html
    # TODO create engine should be base on environment variables or secrets stored in aws for the DEPLOY_ENV passed in environment variables.
    # connection string + pool size + max overflow
    # engine = create_engine('sqlite:///:memory:', echo=True,  pool_size=20, max_overflow=0)
    engine = create_engine('sqlite:///:memory:', echo=True,  pool_size=200)

    # If I don't import user2 does this not create that table?
    # Yes, if I fail to import the user before running this command it is not included.
    Base.metadata.create_all(engine)


    Session = sessionmaker(bind=engine)

    with Session() as session:

        # The reason the commit is necessary for just a simple get is because the session remains open for so long
        user1 = User(name='Alice', email='alice@example.com')
        print('user1')
        user2 = User2(name='Alice', email='alice@example.com')
        print('user1')

        print(user1) # id unknown
        session.add(user1)
        print('added to session but not committed', user1.id) # id unknown and no INSERT INTO called
        # print(user1)
        session.add(user2)

        session.commit() # BEGIN INSERT INTO AND COMMIT ARE ALL CALLED
        print('user.id is now known, no need to force refresh',user1.id)

        session.add(user2)

        session.commit()
        # print(user2)
        session.commit()
        session.commit()

    # really these sessions shouldn't be long lasting, I think they might be in other places
    # session = Session()

    # # 6. Add new data
    # user1 = User(name='Alice', email='alice@example.com')
    # user2 = User(name='Bob', email='bob@example.com')

    # session.add(user1)
    # session.add(user2)
    # session.commit() # Commit the changes to the database


    print("Hello from play-note!")
