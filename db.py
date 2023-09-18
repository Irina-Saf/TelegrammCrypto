from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# PostgreSQL_database = "postgresql://postgres:12345Ok12345@localhost:5433/postgres"
PostgreSQL_database = "postgresql://postgres:12345Ok12345@localhost:5432/CryptoProd"


engine = create_engine(PostgreSQL_database)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
