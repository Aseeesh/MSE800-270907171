"""Seed data for the database"""
 
from datetime import datetime, date, time
from database import db
from models import EnrollmentStatus
from repositories import (
    StudentRepository, LecturerRepository, SubjectRepository,
    EnrollmentRepository, LectureRepository
)

def seed_database():
    """Populate database with sample data"""
    print("🌱 Starting seed...")
    session = db.get_session()
    
    try:
        # Create repositories
        student_repo = StudentRepository(session)
        lecturer_repo = LecturerRepository(session)
        subject_repo = SubjectRepository(session)
        enrollment_repo = EnrollmentRepository(session)
        lecture_repo = LectureRepository(session)
        
        # Check if data already exists
        existing_students = student_repo.get_all()
        if existing_students:
            print(f"⚠️  Data already exists ({len(existing_students)} students found)")
            print("  Clearing existing data...")
            session.query(Enrollment).delete()
            session.query(Lecture).delete()
            session.query(Subject).delete()
            session.query(Lecturer).delete()
            session.query(Student).delete()
            session.commit()
        
        print("  Creating lecturers...")
        lecturer1 = lecturer_repo.create(
            first_name="Dr. Sarah",
            last_name="Johnson",
            lecturer_code="LEC001",
            email="sarah.johnson@university.edu",
            department="Computer Science",
            hire_date=date(2018, 8, 15)
        )
        print(f"    Created: {lecturer1.first_name} {lecturer1.last_name}")
        
        lecturer2 = lecturer_repo.create(
            first_name="Prof. Michael",
            last_name="Chen",
            lecturer_code="LEC002",
            email="michael.chen@university.edu",
            department="Mathematics",
            hire_date=date(2019, 9, 1)
        )
        print(f"    Created: {lecturer2.first_name} {lecturer2.last_name}")
        
        print("  Creating courses...")
        subject1 = subject_repo.create(
            subject_code="CS301",
            subject_name="Database Management Systems",
            units=4,
            description="Introduction to database design and SQL",
            max_students=30,
            lecturer_id=lecturer1.id
        )
        print(f"    Created: {subject1.subject_code} - {subject1.subject_name}")
        
        subject2 = subject_repo.create(
            subject_code="CS302",
            subject_name="Data Structures and Algorithms",
            units=4,
            description="Advanced data structures and algorithm analysis",
            max_students=35,
            lecturer_id=lecturer1.id
        )
        print(f"    Created: {subject2.subject_code} - {subject2.subject_name}")
        
        subject3 = subject_repo.create(
            subject_code="MATH201",
            subject_name="Calculus III",
            units=3,
            description="Multivariable calculus",
            max_students=30,
            lecturer_id=lecturer2.id
        )
        print(f"    Created: {subject3.subject_code} - {subject3.subject_name}")
        
        print("  Creating students...")
        students = []
        student_data = [
            ("John", "Smith", "STU001", "NID12345", date(2000, 5, 15), date(2024, 8, 20), "john.smith@student.edu"),
            ("Emma", "Johnson", "STU002", "NID12346", date(2001, 8, 22), date(2024, 8, 20), "emma.johnson@student.edu"),
            ("Michael", "Williams", "STU003", "NID12347", date(2000, 11, 10), date(2024, 8, 20), "michael.williams@student.edu"),
            ("Sarah", "Brown", "STU004", "NID12348", date(2001, 2, 28), date(2024, 8, 20), "sarah.brown@student.edu"),
            ("David", "Jones", "STU005", "NID12349", date(2000, 9, 5), date(2024, 8, 20), "david.jones@student.edu")
        ]
        
        for data in student_data:
            student = student_repo.create(
                first_name=data[0],
                last_name=data[1],
                student_code=data[2],
                national_id=data[3],
                date_of_birth=data[4],
                date_of_enrolment=data[5],
                email=data[6]
            )
            students.append(student)
            print(f"    Created: {student.student_code} - {student.first_name} {student.last_name}")
        
        print("  Creating enrollments...")
        # Student 1: Enrolled in CS301 and MATH201
        enrollment_repo.create(
            student_id=students[0].id,
            subject_id=subject1.id,
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026
        )
        enrollment_repo.create(
            student_id=students[0].id,
            subject_id=subject3.id,
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026
        )
        
        # Student 2: Enrolled in all 3 subjects
        enrollment_repo.create(
            student_id=students[1].id,
            subject_id=subject1.id,
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026
        )
        enrollment_repo.create(
            student_id=students[1].id,
            subject_id=subject2.id,
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026
        )
        enrollment_repo.create(
            student_id=students[1].id,
            subject_id=subject3.id,
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026
        )
        
        # Student 3: Enrolled in CS302 only
        enrollment_repo.create(
            student_id=students[2].id,
            subject_id=subject2.id,
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026
        )
        
        # Student 4: Enrolled in CS301 and CS302
        enrollment_repo.create(
            student_id=students[3].id,
            subject_id=subject1.id,
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026
        )
        enrollment_repo.create(
            student_id=students[3].id,
            subject_id=subject2.id,
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026
        )
        
        # Student 5: Enrolled in MATH201 only
        enrollment_repo.create(
            student_id=students[4].id,
            subject_id=subject3.id,
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026
        )
        print(f"    Created 9 enrollments")
        
        print("  Creating lectures...")
        lecture_repo.create(
            lecture_code="LEC101",
            lecture_name="Introduction to Database Systems",
            lecture_date=date(2026, 9, 1),
            start_time=time(10, 0),
            end_time=time(11, 30),
            room="Room 201",
            subject_id=subject1.id,
            lecturer_id=lecturer1.id
        )
        
        lecture_repo.create(
            lecture_code="LEC201",
            lecture_name="Introduction to Data Structures",
            lecture_date=date(2026, 9, 2),
            start_time=time(13, 0),
            end_time=time(14, 30),
            room="Room 301",
            subject_id=subject2.id,
            lecturer_id=lecturer1.id
        )
        
        lecture_repo.create(
            lecture_code="LEC301",
            lecture_name="Vectors and 3D Space",
            lecture_date=date(2026, 9, 1),
            start_time=time(15, 0),
            end_time=time(16, 30),
            room="Room 401",
            subject_id=subject3.id,
            lecturer_id=lecturer2.id
        )
        print(f"    Created 3 lectures")
        
        session.commit()
        
        # Get counts
        student_count = student_repo.get_all()
        lecturer_count = lecturer_repo.get_all()
        subject_count = subject_repo.get_all()
        enrollment_count = enrollment_repo.get_all()
        lecture_count = lecture_repo.get_all()
        
        print("\n✅ Database seeded successfully!")
        print(f"  📚 {len(subject_count)} courses")
        print(f"  👨‍🏫 {len(lecturer_count)} lecturers")
        print(f"  👨‍🎓 {len(student_count)} students")
        print(f"  📝 {len(enrollment_count)} enrollments")
        print(f"  🎓 {len(lecture_count)} lectures")
        
        session.close()
        return True
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error seeding database: {str(e)}")
        import traceback
        traceback.print_exc()
        session.close()
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("DATABASE SEED SCRIPT")
    print("=" * 50)
    seed_database()