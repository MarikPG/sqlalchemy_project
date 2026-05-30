from database import session, init_db
from models import Subject, Teacher, Class, Student, Schedule, Grade
import datetime

def add_subject():
    name = input("Назва предмету: ")
    description = input("Опис: ")
    if session.query(Subject).filter_by(name=name).first():
        print("Предмет вже існує!")
        return
    subject = Subject(name=name, description=description)
    session.add(subject)
    session.commit()
    print("Предмет додано!")

def add_teacher():
    first = input("Ім'я: ")
    last = input("Прізвище: ")
    subj_name = input("Предмет: ")
    subject = session.query(Subject).filter_by(name=subj_name).first()
    if not subject:
        print("Предмет не знайдено!")
        return
    teacher = Teacher(first_name=first, last_name=last, subject=subject)
    session.add(teacher)
    session.commit()
    print(" Вчителя додано!")

def add_class():
    name = input("Назва класу: ")
    year = int(input("Рік навчання: "))
    if session.query(Class).filter_by(name=name).first():
        print(" Клас вже існує!")
        return
    school_class = Class(name=name, year=year)
    session.add(school_class)
    session.commit()
    print(" Клас додано!")

def add_student():
    first = input("Ім'я: ")
    last = input("Прізвище: ")
    class_name = input("Клас: ")
    school_class = session.query(Class).filter_by(name=class_name).first()
    if not school_class:
        print("Клас не знайдено!")
        return
    student = Student(first_name=first, last_name=last, school_class=school_class)
    session.add(student)
    session.commit()
    print("Учня додано!")

def add_schedule():
    day = input("День тижня: ")
    time = input("Година (HH:MM): ")
    subj_name = input("Предмет: ")
    class_name = input("Клас: ")
    teacher_name = input("Прізвище вчителя: ")

    subject = session.query(Subject).filter_by(name=subj_name).first()
    school_class = session.query(Class).filter_by(name=class_name).first()
    teacher = session.query(Teacher).filter_by(last_name=teacher_name).first()

    if not subject or not school_class or not teacher:
        print(" Перевірте дані! Предмет, клас або вчитель не знайдені.")
        return

    try:
        parsed_time = datetime.datetime.strptime(time, "%H:%M").time()
        schedule = Schedule(day=day, time=parsed_time,
                            subject=subject, school_class=school_class, teacher=teacher)
        session.add(schedule)
        session.commit()
        print(" Заняття додано!")
    except ValueError:
        print("Неправильний формат часу! Використовуйте HH:MM (наприклад, 08:30)")

def add_grade():
    student_last = input("Прізвище учня: ")
    subj_name = input("Предмет: ")
    value = int(input("Оцінка: "))
    date = input("Дата (YYYY-MM-DD): ")

    student = session.query(Student).filter_by(last_name=student_last).first()
    subject = session.query(Subject).filter_by(name=subj_name).first()

    if not student or not subject:
        print("Перевірте дані! Учень або предмет не знайдені.")
        return

    try:
        parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        grade = Grade(value=value, date=parsed_date, student=student, subject=subject)
        session.add(grade)
        session.commit()
        print("Оцінку додано!")
    except ValueError:
        print(" Неправильний формат дати! Використовуйте YYYY-MM-DD (наприклад, 2026-05-30)")

if __name__ == "__main__":
    init_db()  
    while True:
        print("\nМеню: 1-Предмет 2-Вчитель 3-Клас 4-Учень 5-Розклад 6-Оцінка 0-Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1": add_subject()
        elif choice == "2": add_teacher()
        elif choice == "3": add_class()
        elif choice == "4": add_student()
        elif choice == "5": add_schedule()
        elif choice == "6": add_grade()
        elif choice == "0": 
            print("Вихід з програми...")
            break