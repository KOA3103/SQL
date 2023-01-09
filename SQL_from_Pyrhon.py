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
           id SERIAL PRIMARY KEY,
           first_name VARCHAR(40),
           last_name VARCHAR(40),
           email VARCHAR(40),
           phones VARCHAR(40)
        );
        """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phones(
           id SERIAL PRIMARY KEY,
           phones VARCHAR(40),
           client_id INTEGER not null REFERENCES client (id)
        );
        """)

def add_client(conn):
    client_records = ", ".join(["%s"] * len(client))
    cur.execute((
        f"INSERT INTO client(first_name, last_name, email, phones) "
        f"VALUES {client_records}"
    ), client)

def add_phone(conn):
    phones_records = ", ".join(["%s"] * len(phones))
    cur.execute((
        f"INSERT INTO phones(phones, client_id) "
        f"VALUES {phones_records}"
    ), phones)

# def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
#     pass
#
# def delete_phone(conn, client_id, phone):
#     pass
#
# def delete_client(conn, client_id):
#     pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cur.execute("SELECT c.fist_name, phones from phones p join client c ON c.id = p.client_id GROUP BY p.fist_name, phones")
    print(cur.fetchall())


with psycopg2.connect(database="test", user="postgres", password="5a64Postgres5a64" ) as conn:
    with conn.cursor() as cur:
        conn.autocommit = True
        # create_db(conn)

        client = [
            ("Aaaaa", "AAAAAA", "AaaAAA@gmail.com", "1111"),
            ("Bbbbb", "BBBBBB", "BbbbBBB@gmail.com", "2222"),
            ("Ccccc", "CCCCCC", "CcccCCC@gmail.com", "3333"),
            ("Ddddd", "DDDDDD", "DdddDDD@gmail.com", "4444"),
            ("Eeeee", "EEEEEEE", "EeeeEEE@gamil.com", "5555"),
        ]
        # add_client(conn)

        phones = [
            ("+1111", 1),
            ("+2222", 1),
            ("+3333", 1),
            ("+4444", 2),
            ("+5555", 2),
        ]
        # add_phone(conn)

        find_client("Aaaaa")







