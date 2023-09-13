from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# строка подключения
# PostgreSQL_database = "postgresql://user:password@localhost:5433/database"
# PostgreSQL_database = "postgresql://postgres:12345Ok12345@localhost:5433/postgres"
PostgreSQL_database = "postgresql://postgres:12345Ok12345@localhost:5432/CryptoProd"


# создаем движок SqlAlchemy
engine = create_engine(PostgreSQL_database)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# import psycopg2


# conn = psycopg2.connect(dbname="postgres", user="postgres", password="12345", host="127.0.0.1", port="5432")
# print("Подключение установлено")
# cursor = conn.cursor()

# conn.autocommit = True
# cursor.execute(sql)
# print("База данных успешно создана")

# cursor.close()  # закрываем курсор
# conn.close()    # закрываем подключение
