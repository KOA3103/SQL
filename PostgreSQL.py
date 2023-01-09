# import psycopg2
#
#
# with psycopg2.connect(database="test", user="postgres", password="5a64Postgres5a64") as conn:
#     with conn.cursor() as cur:
#         #удаление таблиц
#         cur.execute("""
#         DROP TABLE homework;
#         DROP TABLE course;
#         """)
#
#         # создание таблиц
#         cur.execute("""
#         CREATE TABLE IF NOT EXISTS course(
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(40) UNIQUE
#         );
#         """)
#         cur.execute("""
#         CREATE TABLE IF NOT EXISTS homework(
#             id SERIAL PRIMARY KEY,
#             number INTEGER NOT NULL,
#             description TEXT NOT NULL,
#             course_id INTEGER NOT NULL REFERENCES course(id)
#         );
#         """)
#         conn.commit()  # фиксируем в БД
#
#         # наполнение таблиц (C из CRUD)
#         cur.execute("""
#         INSERT INTO course(name) VALUES('Python') RETURNING id, name;
#         """)
#         conn.commit()  # фиксируем в БД
#         print(cur.fetchone())  # запрос данных автоматически зафиксирует изменения
#
#         cur.execute("""
#         INSERT INTO course(name) VALUES('Java') RETURNING id, name;
#         """)
#         print(cur.fetchone())  # запрос данных автоматически зафиксирует изменения
#
#         cur.execute("""
#         INSERT INTO homework(number, description, course_id) VALUES(1, 'простое дз', 1) RETURNING number, description, course_id;
#         """)
#         # conn.commit()  # фиксируем в БД
#         print(cur.fetchone())  # запрос данных автоматически зафиксирует изменения

        # извлечение данных (R из CRUD)
        # cur.execute("""
        # SELECT * FROM course;
        # """)
        # print('fetchall', cur.fetchall())  # извлечь все строки
        #
        # cur.execute("""
        # SELECT * FROM course;
        # """)
        # print(cur.fetchone())  # извлечь первую строку (аналог LIMIT 1)
        #
        # cur.execute("""
        # SELECT * FROM course;
        # """)
        # print(cur.fetchmany(3))  # извлечь первые N строк (аналог LIMIT N)

        # cur.execute("""
        # SELECT name FROM course;
        # """)
        # print(cur.fetchall())
        #
        # cur.execute("""
        # SELECT id FROM course WHERE name='Python';
        # """)
        # print(cur.fetchone())

        # cur.execute("""
        # SELECT id FROM course WHERE name='{}';
        # """.format("Python"))  # плохо - возможна SQL инъекция
        # print(cur.fetchone())

        # cur.execute("""
        # SELECT id FROM course WHERE name=%s;
        # """, ("Python",))  # хорошо, обратите внимание на кортеж
        # print(cur.fetchone())

        # def get_course_id(cursor, name: str) -> int:
        #     cursor.execute("""
        #     SELECT id, name FROM course WHERE name=%s;
        #     """, (name,))
        #     return cur.fetchall()[0][1]
        # # python_id = get_course_id(cur, 'Python')
        # # print('python_id пайтон номер', python_id)
        # print('python_id пайтон номер', get_course_id(cur, 'Python'))

        # cur.execute("""
        # INSERT INTO homework(number, description, course_id) VALUES(%s, %s, %s);
        # """, (2, "задание посложнее", 1))
        # conn.commit()  # фиксируем в БД
        #
        # cur.execute("""
        # SELECT * FROM homework;
        # """)
        # print(cur.fetchall()[1][2])

        # обновление данных (U из CRUD)
        # cur.execute("""
        # UPDATE course SET name=%s WHERE id=%s;
        # """, ('Python Advanced', 2))
        # cur.execute("""
        # SELECT * FROM course;
        # """)
        # print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения

        # # удаление данных (D из CRUD)
        # cur.execute("""
        # DELETE FROM homework WHERE id=%s;
        # """, (1,))
        # cur.execute("""
        # SELECT * FROM homework;
        # """)
        # print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения

# conn.close()

# import pyautogui
# import time
# while True:
#     pyautogui.moveRel(5, 10)
#     time.sleep(1)

# a, *b, c, d = [1, 3, 'f']
# print(a)
# print(b)
# print(c)
# print(d)


#
# print(ord("5")+ord("a")+ord("6")+ord("4"))
# print(ord("5")+ord("a")+ord("6")+ord("4"))
# print(ord("a"), ord("а"), ord("a"), ord("а"), ord("a"), ord("а"))
#
#
# print(chr(888), chr(1666))

import urllib.parse
print(urllib.parse.quote_plus("%/Postgres/%"))