import psycopg2


def create_db(conn):
    # удаление таблиц
    cur.execute("""
        DROP TABLE phones;
        DROP TABLE client;
        """)

    # создание таблиц
    cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
           id SERIAL NOT NULL PRIMARY KEY,
           first_name VARCHAR(40),
           last_name VARCHAR(40),
           email VARCHAR(40)
        );
        """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phones(
           id SERIAL PRIMARY KEY,
           phones VARCHAR(40),
           client_id INTEGER REFERENCES client(id)
        );
        """)

def add_client(conn, first_name, last_name, email, phones=None, client_id=None):
    cur.execute(""" INSERT INTO client(first_name, last_name, email) VALUES(%s, %s, %s);
        """, (first_name, last_name, email))
    cur.execute(""" INSERT INTO phones(phones, client_id) VALUES(%s, %s);
                """, (phones, client_id))

def add_phone(conn, client_id, phones):
    cur.execute(""" INSERT INTO phones(phones, client_id) VALUES(%s, %s);
            """, (client_id, phones))

# def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
#     pass
#
# def delete_phone(conn, client_id, phone):
#     pass
#
# def delete_client(conn, client_id):
#     pass
#
# def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
#     pass

with psycopg2.connect(database="test", user="postgres", password="5a64Postgres5a64" ) as conn:
    with conn.cursor() as cur:
        conn.autocommit = True
        # create_db(conn)
        # add_client(conn, "4Dima", "Sidorov4", "4DimaSidorov@gmail.com", "44444444")
        add_phone(conn, "3333333", 4)



