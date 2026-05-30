from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
# ЗМІНЕНО: Імпортуємо Base з файлу database.py
from database import Base

class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    
    teachers = relationship("Teacher", back_populates="subject")
    schedules = relationship("Schedule", back_populates="subject")
    grades = relationship("Grade", back_populates="subject")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    subject_id = Column(ForeignKey('subjects.id'))
    
    subject = relationship("Subject", back_populates="teachers")
    schedules = relationship("Schedule", back_populates="teacher")

class Class(Base):
    __tablename__ = 'classes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    
    students = relationship("Student", back_populates="school_class")
    schedules = relationship("Schedule", back_populates="school_class")

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    class_id = Column(ForeignKey('classes.id'))
    
    school_class = relationship("Class", back_populates="students")
    grades = relationship("Grade", back_populates="student")

class Schedule(Base):
    __tablename__ = 'schedules'
    
    id = Column(Integer, primary_key=True)
    day = Column(String, nullable=False)
    time = Column(Time, nullable=False)
    subject_id = Column(ForeignKey('subjects.id'))
    class_id = Column(ForeignKey('classes.id'))
    teacher_id = Column(ForeignKey('teachers.id'))
    
    subject = relationship("Subject", back_populates="schedules")
    school_class = relationship("Class", back_populates="schedules")
    teacher = relationship("Teacher", back_populates="schedules")

class Grade(Base):
    __tablename__ = 'grades'
    
    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    student_id = Column(ForeignKey('students.id'))
    subject_id = Column(ForeignKey('subjects.id'))
    
    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")