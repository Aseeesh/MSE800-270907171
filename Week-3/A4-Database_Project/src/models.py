"""SQLAlchemy ORM Models"""
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Enum, Float, Time, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum

Base = declarative_base()

class BaseModel(Base):
    """Base model with common fields"""
    __abstract__ = True
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(Date, default=datetime.now)
    updated_at = Column(Date, default=datetime.now, onupdate=datetime.now)

class EnrollmentStatus(enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    DROPPED = "dropped"

class Student(BaseModel):
    __tablename__ = 'students'
    
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    student_code = Column(String(20), unique=True, nullable=False)
    national_id = Column(String(20), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    date_of_enrolment = Column(Date, nullable=False)
    email = Column(String(100), unique=True)
    
    enrollments = relationship("Enrollment", back_populates="student")
    
    def __repr__(self):
        return f"Student({self.student_code}: {self.first_name} {self.last_name})"

class Lecturer(BaseModel):
    __tablename__ = 'lecturers'
    
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    lecturer_code = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    department = Column(String(100), nullable=False)
    hire_date = Column(Date, nullable=False)
    
    subjects = relationship("Subject", back_populates="lecturer")
    
    def __repr__(self):
        return f"Lecturer({self.lecturer_code}: {self.first_name} {self.last_name})"

class Subject(BaseModel):
    __tablename__ = 'subjects'
    
    subject_code = Column(String(20), unique=True, nullable=False)
    subject_name = Column(String(200), nullable=False)
    units = Column(Integer, nullable=False, default=3)
    description = Column(Text)
    max_students = Column(Integer, default=30)
    
    lecturer_id = Column(String(36), ForeignKey('lecturers.id'), nullable=False)
    
    lecturer = relationship("Lecturer", back_populates="subjects")
    enrollments = relationship("Enrollment", back_populates="subject")
    
    def __repr__(self):
        return f"Subject({self.subject_code}: {self.subject_name})"

class Enrollment(BaseModel):
    __tablename__ = 'enrollments'
    
    student_id = Column(String(36), ForeignKey('students.id'), nullable=False)
    subject_id = Column(String(36), ForeignKey('subjects.id'), nullable=False)
    
    enrollment_date = Column(Date, nullable=False)
    status = Column(Enum(EnrollmentStatus), default=EnrollmentStatus.ACTIVE)
    semester = Column(String(20), nullable=False)
    year = Column(Integer, nullable=False)
    grade = Column(String(2))
    
    student = relationship("Student", back_populates="enrollments")
    subject = relationship("Subject", back_populates="enrollments")
    
    def __repr__(self):
        return f"Enrollment({self.student_id} -> {self.subject_id})"

class Lecture(BaseModel):
    __tablename__ = 'lectures'
    
    subject_id = Column(String(36), ForeignKey('subjects.id'), nullable=False)
    lecturer_id = Column(String(36), ForeignKey('lecturers.id'), nullable=False)
    
    lecture_code = Column(String(20), unique=True, nullable=False)
    lecture_name = Column(String(200), nullable=False)
    lecture_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    room = Column(String(50), nullable=False)
    
    subject = relationship("Subject")
    lecturer = relationship("Lecturer")
    
    def __repr__(self):
        return f"Lecture({self.lecture_code}: {self.lecture_name})"