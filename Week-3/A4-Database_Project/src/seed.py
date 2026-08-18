"""Seed data for the database - Matches ER Diagram"""
from datetime import datetime, date, time
from database import db
from models import EnrollmentStatus
from repositories import (
    StudentRepository, LecturerRepository, SubjectRepository,
    EnrollmentRepository, LectureRepository
)

def seed_database():
    """Populate database with sample data matching ER diagram"""
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
        
        # 1. Create LECTURERS (matches ER diagram)
        print("  Creating lecturers...")
        lecturer1 = lecturer_repo.create(
            first_name="Dr. Sarah",
            last_name="Johnson",
            lecturer_code="LEC001",
            email="sarah.johnson@university.edu",
            phone="+1234567890",
            address="123 Faculty Building, Room 101",
            department="Computer Science",
            hire_date=date(2018, 8, 15),
            specialization="Database Systems"
        )
        print(f"    Created: {lecturer1.first_name} {lecturer1.last_name}")
        
        lecturer2 = lecturer_repo.create(
            first_name="Prof. Michael",
            last_name="Chen",
            lecturer_code="LEC002",
            email="michael.chen@university.edu",
            phone="+1234567891",
            address="123 Faculty Building, Room 202",
            department="Mathematics",
            hire_date=date(2019, 9, 1),
            specialization="Applied Mathematics"
        )
        print(f"    Created: {lecturer2.first_name} {lecturer2.last_name}")
        
        # 2. Create SUBJECTS (matches ER diagram)
        print("  Creating subjects...")
        subject1 = subject_repo.create(
            subject_code="CS301",
            subject_name="Database Management Systems",
            units=4,
            description="Introduction to database design, SQL, and management",
            level="Undergraduate",
            max_students=30,
            lecturer_id=lecturer1.id  # FK to LECTURER
        )
        print(f"    Created: {subject1.subject_code} - {subject1.subject_name}")
        
        subject2 = subject_repo.create(
            subject_code="CS302",
            subject_name="Data Structures and Algorithms",
            units=4,
            description="Advanced data structures and algorithm analysis",
            level="Undergraduate",
            max_students=35,
            lecturer_id=lecturer1.id  # FK to LECTURER
        )
        print(f"    Created: {subject2.subject_code} - {subject2.subject_name}")
        
        subject3 = subject_repo.create(
            subject_code="MATH201",
            subject_name="Calculus III",
            units=3,
            description="Multivariable calculus and differential equations",
            level="Undergraduate",
            max_students=30,
            lecturer_id=lecturer2.id  # FK to LECTURER
        )
        print(f"    Created: {subject3.subject_code} - {subject3.subject_name}")
        
        # 3. Create STUDENTS (matches ER diagram)
        print("  Creating students...")
        students = []
        student_data = [
            ("John", "Smith", "STU001", "NID12345", date(2000, 5, 15), date(2024, 8, 20), "john.smith@student.edu", "+1234567892", "123 Student Dorm, Room 101"),
            ("Emma", "Johnson", "STU002", "NID12346", date(2001, 8, 22), date(2024, 8, 20), "emma.johnson@student.edu", "+1234567893", "123 Student Dorm, Room 102"),
            ("Michael", "Williams", "STU003", "NID12347", date(2000, 11, 10), date(2024, 8, 20), "michael.williams@student.edu", "+1234567894", "123 Student Dorm, Room 103"),
            ("Sarah", "Brown", "STU004", "NID12348", date(2001, 2, 28), date(2024, 8, 20), "sarah.brown@student.edu", "+1234567895", "123 Student Dorm, Room 104"),
            ("David", "Jones", "STU005", "NID12349", date(2000, 9, 5), date(2024, 8, 20), "david.jones@student.edu", "+1234567896", "123 Student Dorm, Room 105")
        ]
        
        for data in student_data:
            student = student_repo.create(
                first_name=data[0],
                last_name=data[1],
                student_code=data[2],
                national_id=data[3],
                date_of_birth=data[4],
                date_of_enrolment=data[5],
                email=data[6],
                phone=data[7],
                address=data[8]
            )
            students.append(student)
            print(f"    Created: {student.student_code} - {student.first_name} {student.last_name}")
        
        # 4. Create ENROLLMENTS (matches ER diagram: STUDENT ||--o{ ENROLLMENT, SUBJECT ||--o{ ENROLLMENT)
        print("  Creating enrollments...")
        
        # Student 1: Enrolled in CS301 and MATH201
        enrollment_repo.create(
            student_id=students[0].id,  # FK to STUDENT
            subject_id=subject1.id,      # FK to SUBJECT
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026,
            attendance_percentage=85
        )
        enrollment_repo.create(
            student_id=students[0].id,  # FK to STUDENT
            subject_id=subject3.id,      # FK to SUBJECT
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026,
            attendance_percentage=90
        )
        
        # Student 2: Enrolled in all 3 subjects
        enrollment_repo.create(
            student_id=students[1].id,  # FK to STUDENT
            subject_id=subject1.id,      # FK to SUBJECT
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026,
            attendance_percentage=95
        )
        enrollment_repo.create(
            student_id=students[1].id,  # FK to STUDENT
            subject_id=subject2.id,      # FK to SUBJECT
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026,
            attendance_percentage=88
        )
        enrollment_repo.create(
            student_id=students[1].id,  # FK to STUDENT
            subject_id=subject3.id,      # FK to SUBJECT
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026,
            attendance_percentage=92
        )
        
        # Student 3: Enrolled in CS302 only
        enrollment_repo.create(
            student_id=students[2].id,  # FK to STUDENT
            subject_id=subject2.id,      # FK to SUBJECT
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026,
            attendance_percentage=75
        )
        
        # Student 4: Enrolled in CS301 and CS302
        enrollment_repo.create(
            student_id=students[3].id,  # FK to STUDENT
            subject_id=subject1.id,      # FK to SUBJECT
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026,
            attendance_percentage=80
        )
        enrollment_repo.create(
            student_id=students[3].id,  # FK to STUDENT
            subject_id=subject2.id,      # FK to SUBJECT
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026,
            attendance_percentage=85
        )
        
        # Student 5: Enrolled in MATH201 only
        enrollment_repo.create(
            student_id=students[4].id,  # FK to STUDENT
            subject_id=subject3.id,      # FK to SUBJECT
            enrollment_date=date(2026, 8, 20),
            status=EnrollmentStatus.ACTIVE,
            semester="Fall 2026",
            year=2026,
            attendance_percentage=70
        )
        print(f"    Created 9 enrollments")
        
        # 5. Create LECTURES (matches ER diagram: SUBJECT ||--o{ LECTURE, LECTURER ||--o{ LECTURE)
        print("  Creating lectures...")
        
        # CS301 Lectures (Subject 1)
        lecture_repo.create(
            lecture_code="LEC101",
            lecture_name="Introduction to Database Systems",
            lecture_date=date(2026, 9, 1),
            start_time=time(10, 0),
            end_time=time(11, 30),
            day_of_week="Monday",
            room="Room 201",
            building="Science Building",
            capacity=30,
            subject_id=subject1.id,    # FK to SUBJECT
            lecturer_id=lecturer1.id   # FK to LECTURER
        )
        
        lecture_repo.create(
            lecture_code="LEC102",
            lecture_name="Relational Model and SQL",
            lecture_date=date(2026, 9, 3),
            start_time=time(10, 0),
            end_time=time(11, 30),
            day_of_week="Wednesday",
            room="Room 201",
            building="Science Building",
            capacity=30,
            subject_id=subject1.id,    # FK to SUBJECT
            lecturer_id=lecturer1.id   # FK to LECTURER
        )
        
        lecture_repo.create(
            lecture_code="LEC103",
            lecture_name="Database Design",
            lecture_date=date(2026, 9, 8),
            start_time=time(10, 0),
            end_time=time(11, 30),
            day_of_week="Monday",
            room="Room 201",
            building="Science Building",
            capacity=30,
            subject_id=subject1.id,    # FK to SUBJECT
            lecturer_id=lecturer1.id   # FK to LECTURER
        )
        
        # CS302 Lectures (Subject 2)
        lecture_repo.create(
            lecture_code="LEC201",
            lecture_name="Arrays and Linked Lists",
            lecture_date=date(2026, 9, 2),
            start_time=time(13, 0),
            end_time=time(14, 30),
            day_of_week="Tuesday",
            room="Room 301",
            building="Science Building",
            capacity=35,
            subject_id=subject2.id,    # FK to SUBJECT
            lecturer_id=lecturer1.id   # FK to LECTURER
        )
        
        lecture_repo.create(
            lecture_code="LEC202",
            lecture_name="Stacks and Queues",
            lecture_date=date(2026, 9, 4),
            start_time=time(13, 0),
            end_time=time(14, 30),
            day_of_week="Thursday",
            room="Room 301",
            building="Science Building",
            capacity=35,
            subject_id=subject2.id,    # FK to SUBJECT
            lecturer_id=lecturer1.id   # FK to LECTURER
        )
        
        lecture_repo.create(
            lecture_code="LEC203",
            lecture_name="Trees and Graphs",
            lecture_date=date(2026, 9, 9),
            start_time=time(13, 0),
            end_time=time(14, 30),
            day_of_week="Tuesday",
            room="Room 301",
            building="Science Building",
            capacity=35,
            subject_id=subject2.id,    # FK to SUBJECT
            lecturer_id=lecturer1.id   # FK to LECTURER
        )
        
        # MATH201 Lectures (Subject 3)
        lecture_repo.create(
            lecture_code="LEC301",
            lecture_name="Vectors and 3D Space",
            lecture_date=date(2026, 9, 1),
            start_time=time(15, 0),
            end_time=time(16, 30),
            day_of_week="Monday",
            room="Room 401",
            building="Math Building",
            capacity=30,
            subject_id=subject3.id,    # FK to SUBJECT
            lecturer_id=lecturer2.id   # FK to LECTURER
        )
        
        lecture_repo.create(
            lecture_code="LEC302",
            lecture_name="Partial Derivatives",
            lecture_date=date(2026, 9, 3),
            start_time=time(15, 0),
            end_time=time(16, 30),
            day_of_week="Wednesday",
            room="Room 401",
            building="Math Building",
            capacity=30,
            subject_id=subject3.id,    # FK to SUBJECT
            lecturer_id=lecturer2.id   # FK to LECTURER
        )
        
        lecture_repo.create(
            lecture_code="LEC303",
            lecture_name="Multiple Integrals",
            lecture_date=date(2026, 9, 8),
            start_time=time(15, 0),
            end_time=time(16, 30),
            day_of_week="Monday",
            room="Room 401",
            building="Math Building",
            capacity=30,
            subject_id=subject3.id,    # FK to SUBJECT
            lecturer_id=lecturer2.id   # FK to LECTURER
        )
        print(f"    Created 9 lectures")
        
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