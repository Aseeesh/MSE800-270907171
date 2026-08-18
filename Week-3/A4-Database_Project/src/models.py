"""SQLAlchemy ORM Models - Optimized University Database"""
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Enum, Time, Text, DateTime
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
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class EnrollmentStatus(enum.Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    DROPPED = "dropped"
    FAILED = "failed"

class Student(BaseModel):
    __tablename__ = 'students'
    
    # Student fields - matches ER diagram
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    student_code = Column(String(20), unique=True, nullable=False, index=True)
    national_id = Column(String(20), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    date_of_enrolment = Column(Date, nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    address = Column(String(200))
    
    # Relationships  
    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"Student({self.student_code}: {self.first_name} {self.last_name})"

class Lecturer(BaseModel):
    __tablename__ = 'lecturers'
    
    # Lecturer fields - matches ER diagram
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    lecturer_code = Column(String(20), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(200))
    department = Column(String(100), nullable=False)
    hire_date = Column(Date, nullable=False)
    specialization = Column(String(100))
    
    # Relationships - matches ER diagram: LECTURER ||--o{ SUBJECT and LECTURER ||--o{ LECTURE
    subjects = relationship("Subject", back_populates="lecturer")
    lectures = relationship("Lecture", back_populates="lecturer")
    
    def __repr__(self):
        return f"Lecturer({self.lecturer_code}: {self.first_name} {self.last_name})"

class Subject(BaseModel):
    __tablename__ = 'subjects'
    
    # Subject fields - matches ER diagram
    subject_code = Column(String(20), unique=True, nullable=False, index=True)
    subject_name = Column(String(200), nullable=False)
    units = Column(Integer, nullable=False, default=3)
    description = Column(Text)
    level = Column(String(20))
    max_students = Column(Integer, default=30)
    
    # Foreign Key - matches ER diagram: lecturer_id FK
    lecturer_id = Column(String(36), ForeignKey('lecturers.id'), nullable=False)
    
    # Relationships - matches ER diagram: LECTURER ||--o{ SUBJECT, SUBJECT ||--o{ ENROLLMENT, SUBJECT ||--o{ LECTURE
    lecturer = relationship("Lecturer", back_populates="subjects")
    enrollments = relationship("Enrollment", back_populates="subject", cascade="all, delete-orphan")
    lectures = relationship("Lecture", back_populates="subject", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"Subject({self.subject_code}: {self.subject_name})"

class Enrollment(BaseModel):
    __tablename__ = 'enrollments'
    
    # Foreign Keys - matches ER diagram: student_id FK, subject_id FK
    student_id = Column(String(36), ForeignKey('students.id'), nullable=False, index=True)
    subject_id = Column(String(36), ForeignKey('subjects.id'), nullable=False, index=True)
    
    # Enrollment fields - matches ER diagram
    enrollment_date = Column(Date, nullable=False)
    status = Column(Enum(EnrollmentStatus), default=EnrollmentStatus.ACTIVE)
    semester = Column(String(20), nullable=False)
    year = Column(Integer, nullable=False)
    grade = Column(String(2))
    grade_points = Column(Integer, default=0)
    attendance_percentage = Column(Integer, default=0)
    
    # Relationships - matches ER diagram: STUDENT ||--o{ ENROLLMENT, SUBJECT ||--o{ ENROLLMENT
    student = relationship("Student", back_populates="enrollments")
    subject = relationship("Subject", back_populates="enrollments")
    
    def __repr__(self):
        return f"Enrollment({self.student_id} -> {self.subject_id})"

class Lecture(BaseModel):
    __tablename__ = 'lectures'
    
    # Foreign Keys - matches ER diagram: subject_id FK, lecturer_id FK
    subject_id = Column(String(36), ForeignKey('subjects.id'), nullable=False, index=True)
    lecturer_id = Column(String(36), ForeignKey('lecturers.id'), nullable=False, index=True)
    
    # Lecture fields - matches ER diagram
    lecture_code = Column(String(20), unique=True, nullable=False, index=True)
    lecture_name = Column(String(200), nullable=False)
    lecture_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    day_of_week = Column(String(20), nullable=False)
    room = Column(String(50), nullable=False)
    building = Column(String(50))
    capacity = Column(Integer, default=30)
    
    # Relationships - matches ER diagram: SUBJECT ||--o{ LECTURE, LECTURER ||--o{ LECTURE
    subject = relationship("Subject", back_populates="lectures")
    lecturer = relationship("Lecturer", back_populates="lectures")
    
    def __repr__(self):
        return f"Lecture({self.lecture_code}: {self.lecture_name})"