import pymysql
import pytest


host = '52.29.239.198'
user = 'sql7746562'
password = '5hZtCuyTwN'
db_name = 'sql7746562'

@pytest.fixture()
def connect_db():   
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        yield connection  
    except Exception as ex:
        print("Connection refused...")
        print(ex)
        yield None 


@pytest.fixture()
def fetch_superhero_names(connect_db):   
    connection = connect_db
    if connection is not None:  
        try:
            with connection.cursor() as cursor:
                select_all_rows = "SELECT name FROM superheroes"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                return [row['name'] for row in rows]  
        finally:
            connection.close() 
    else:
        print("Connection refused...")
        return [] 