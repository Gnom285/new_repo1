import pytest
from sqlalchemy.orm import sessionmaker
from models import engine, Base

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.create_all(engine)

@pytest.fixture
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session

    session.close()
    transaction.rollback()
    connection.close()