"""Repository pattern for database operations"""
from sqlalchemy.orm import Session
from typing import List
from models import Student, Lecturer, Subject, Enrollment, Lecture

class BaseRepository:
    """Base repository with common CRUD operations"""
    def __init__(self, model, session: Session):
        self.model = model
        self.session = session
    
    def create(self, **kwargs):
        """Create a new record"""
        instance = self.model(**kwargs)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance
    
    def get_all(self) -> List:
        """Get all records"""
        return self.session.query(self.model).all()
    
    def get_by_id(self, id: str):
        """Get record by ID"""
        return self.session.query(self.model).filter(self.model.id == id).first()
    
    def find_by(self, **filters) -> List:
        """Find records by filters"""
        query = self.session.query(self.model)
        for key, value in filters.items():
            if hasattr(self.model, key):
                query = query.filter(getattr(self.model, key) == value)
        return query.all()

class StudentRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(Student, session)
    
    def get_by_student_code(self, code: str):
        return self.session.query(Student).filter(Student.student_code == code).first()

class LecturerRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(Lecturer, session)

class SubjectRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(Subject, session)

class EnrollmentRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(Enrollment, session)

class LectureRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(Lecture, session)