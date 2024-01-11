import pytest
from sqlalchemy import create_engine
from utilities.readProperties import ReadConfig

@pytest.fixture
def db_engine():
    server = ReadConfig.getServername()
    database = ReadConfig.getDatabasename()
    engine = create_engine(f"mssql+pyodbc://{server}/{database}?driver=SQL+Server")
    return engine


