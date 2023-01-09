import sqlalchemy
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Course(Base):
    __tablename__ = "course"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    homework = relationship("Homework", back_populates="course")
    # homework = relationship("Homework", backref="course")
    def __str__(self):
        return f'Course {self.id}: -> {self.name}'

class Homework(Base):
    __tablename__ = "homework"
    id = sq.Column(sq.Integer, primary_key=True)
    number = sq.Column(sq.Integer, nullable=False)
    description = sq.Column(sq.Text, nullable=False)
    course_id = sq.Column(sq.Integer, sq.ForeignKey("course.id"), nullable=False)
    course = relationship("Course", back_populates="homework")
    # course = relationship("Course", backref="homeworks")

    def __str__(self):
        return f'Homework id:{self.id} -> (number: {self.number},{self.description}), course_id: {self.course_id}'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


DSN = 'postgresql://postgres:5a64Postgres5a64@localhost:5432/test'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# создание объектов
course1 = Course(name="Python")
course2 = Course(name="Jawa")
course3 = Course(name="C++")

print(course1.id)

session.add_all([course1, course2, course3])
session.commit() # фиксируем изменения
print(course1.id, course2.id, course3.id)

# создание объектов
hw1 = Homework(number=1, description='простая дз', course_id=1)
hw2 = Homework(number=2, description='сложное дз', course_id=2)
session.add_all([hw1, hw2]) # добавляем all
# session.add(hw1) # добавляем по одному за раз
# session.add(hw2)
session.commit() # фиксируем изменения

# запросы
# for i in session.query(Course).all():
#     print(i)
# for i in session.query(Homework).filter(Homework.number > 1).all():
#     print(i)

# for i in session.query(Homework).filter(Homework.description.like('%сл%')).all():
#     print(i)

# for i in session.query(Course).join(Homework.course).filter(Homework.number == 1).all():
# for i in session.query(Course).join(Homework.course).all():
#     print(i)

# q = session.query(Course).join(Homework.course).filter(Homework.number == 1)
# print(q)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.homework:
#         print("\t", hw.id, hw.number, hw.description)

# вложенный запрос
# subq = session.query(Homework).filter(Homework.description.like("%сложн%")).subquery()
# q = session.query(Course).join(subq, Course.id == subq.c.course_id)
# # print(subq)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.homework:
#         print("\t", hw.id, hw.number, hw.description)

# обновление объектов
session.query(Course).filter(Course.name == "Jawa").update({"name": "NEW JavaScript"})
session.commit()  # фиксируем изменения

session.query(Homework).filter(Homework.description == "сложное дз").update({"number": 3})
session.commit()  # фиксируем изменения

session.query(Homework).filter(Homework.description == "сложное дз").update({"description": "не выполнимое"})
session.commit()  # фиксируем изменения

# удаление объектов
session.query(Homework).filter(Homework.number > 1).delete()
session.commit()  # фиксируем изменения

session.query(Course).filter(Course.name == "C++").delete()
session.commit()  # фиксируем изменения

for i in session.query(Homework).all():
    print(i)

for i in session.query(Course).all():
    print(i)

session.close()