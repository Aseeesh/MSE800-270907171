"""Main application - Run queries and test the database"""
from sqlalchemy import func
from database import db
from models import Student, Subject, Enrollment, Lecturer

def run_queries():
    """Run the required queries"""
    session = db.get_session()
    
    print("\n" + "=" * 60)
    print("UNIVERSITY DATABASE QUERIES")
    print("=" * 60)
    
    # Query 1: How many students are registered in each course?
    print("\n📊 QUERY 1: Students registered in each course")
    print("-" * 40)
    
    results = session.query(
        Subject.subject_code,
        Subject.subject_name,
        func.count(Enrollment.student_id).label('student_count')
    ).join(Enrollment).group_by(Subject.id).all()
    
    if results:
        for row in results:
            print(f"  {row.subject_code} - {row.subject_name}: {row.student_count} students")
    else:
        print("  No enrollments found")
    
    # Query 2: Students enrolled in more than one course
    print("\n📊 QUERY 2: Students enrolled in more than one course")
    print("-" * 40)
    
    results = session.query(
        Student.student_code,
        Student.first_name,
        Student.last_name,
        func.count(Enrollment.subject_id).label('course_count')
    ).join(Enrollment).group_by(Student.id).having(
        func.count(Enrollment.subject_id) > 1
    ).all()
    
    if results:
        print("  Students enrolled in more than one course:")
        for row in results:
            print(f"    {row.student_code}: {row.first_name} {row.last_name} - {row.course_count} courses")
    else:
        print("  No students enrolled in more than one course")
    
    # Additional Info: Show all enrollments (FIXED)
    print("\n📊 BONUS: All Enrollments")
    print("-" * 40)
    
    # Fixed query with proper joins
    results = session.query(
        Student.student_code,
        Student.first_name,
        Student.last_name,
        Subject.subject_code,
        Subject.subject_name,
        Enrollment.semester,
        Enrollment.year
    ).select_from(Enrollment).join(Student).join(Subject).order_by(Student.student_code).all()
    
    if results:
        current_student = None
        for row in results:
            if current_student != row.student_code:
                if current_student:
                    print()
                print(f"  {row.student_code}: {row.first_name} {row.last_name}")
                current_student = row.student_code
            print(f"    - {row.subject_code}: {row.subject_name} ({row.semester} {row.year})")
    else:
        print("  No enrollments found")
    
    # Summary Statistics
    print("\n📊 SUMMARY STATISTICS")
    print("-" * 40)
    
    total_students = session.query(Student).count()
    total_subjects = session.query(Subject).count()
    total_enrollments = session.query(Enrollment).count()
    total_lecturers = session.query(Lecturer).count()
    
    print(f"  Total Students: {total_students}")
    print(f"  Total Lecturers: {total_lecturers}")
    print(f"  Total Courses: {total_subjects}")
    print(f"  Total Enrollments: {total_enrollments}")
    
    if total_students > 0:
        print(f"  Average enrollments per student: {total_enrollments / total_students:.1f}")
    
    session.close()
    
    print("\n" + "=" * 60)
    print("✅ Query execution completed!")
    print("=" * 60)

def check_database():
    """Check if database has data"""
    session = db.get_session()
    
    student_count = session.query(Student).count()
    lecturer_count = session.query(Lecturer).count()
    subject_count = session.query(Subject).count()
    enrollment_count = session.query(Enrollment).count()
    
    print("\n🔍 DATABASE STATUS CHECK")
    print("=" * 60)
    print(f"  Students: {student_count}")
    print(f"  Lecturers: {lecturer_count}")
    print(f"  Subjects: {subject_count}")
    print(f"  Enrollments: {enrollment_count}")
    
    if student_count == 0:
        print("\n⚠️  No data found! Please run: python src/seed.py")
        print("=" * 60)
        session.close()
        return False
    else:
        print("\n✅ Database has data!")
        print("=" * 60)
        session.close()
        return True

def show_sample_data():
    """Show sample data from each table"""
    session = db.get_session()
    
    print("\n📋 SAMPLE DATA")
    print("=" * 60)
    
    # Show students
    print("\n👨‍🎓 Students:")
    students = session.query(Student).limit(5).all()
    if students:
        for s in students:
            print(f"  {s.student_code}: {s.first_name} {s.last_name} (DOB: {s.date_of_birth})")
    else:
        print("  No students found")
    
    # Show lecturers
    print("\n👨‍🏫 Lecturers:")
    lecturers = session.query(Lecturer).limit(5).all()
    if lecturers:
        for l in lecturers:
            print(f"  {l.lecturer_code}: {l.first_name} {l.last_name} - {l.department}")
    else:
        print("  No lecturers found")
    
    # Show subjects
    print("\n📚 Subjects:")
    subjects = session.query(Subject).limit(5).all()
    if subjects:
        for s in subjects:
            lecturer = session.query(Lecturer).filter(Lecturer.id == s.lecturer_id).first()
            if lecturer:
                print(f"  {s.subject_code}: {s.subject_name} (Units: {s.units}) - Lecturer: {lecturer.first_name} {lecturer.last_name}")
            else:
                print(f"  {s.subject_code}: {s.subject_name} (Units: {s.units})")
    else:
        print("  No subjects found")
    
    session.close()

def main():
    """Main entry point"""
    print("🚀 Starting University Database Application")
    print("=" * 60)
    
    # Check if database has data
    if not check_database():
        return
    
    # Show sample data
    show_sample_data()
    
    # Run queries
    run_queries()
    
    print("\n✨ Application completed successfully!")

if __name__ == "__main__":
    main()