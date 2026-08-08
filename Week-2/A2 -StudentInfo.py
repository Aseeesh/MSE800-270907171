# ==============================================================================
# (get_info) of an individual student into a single unit.
# ==============================================================================
class Student:
    def __init__(self, name: str,student_id: int, age: int,address: str = None):
        self.name = name  # Property
        self.student_id = student_id  # Property
        self.age = age    # Property
        self.address = address  # Placeholder for future expansion (e.g., address attribute)

    def get_info(self) -> str:
        """Returns a formatted string of student details."""
        if self.address:
            return f"Name: {self.name:<15} | ID: {self.student_id} | Age: {self.age} | Address: {self.address}"
        return f"Name: {self.name:<15} | ID: {self.student_id} | Age: {self.age}"

# ============================================================================== 
# sorting algorithms, and user input validation behind clear methods.
# ==============================================================================
class StudentManager:
    def __init__(self):
        self.student_list = []  # Stores instances of Student objects

    def add_student(self):
        """Prompts user for details, validates input, and creates a Student object."""
        print("\n--- Enter Student Details ---")
        name = input("Enter student name: ").strip()

        # TRY-EXCEPT: Input validation for age
        while True:
            try:
                age = int(input("Enter student age: "))
                if age <= 0:
                    print("Age must be greater than 0. Try again.")
                    continue
                break  # Exit loop if age is valid
            except ValueError:
                print("Error: Please enter a valid integer for age.")

        # Creating a new Student object using the validated inputs
        address = input("Enter student address (optional): ").strip()
        while True:
            try:
                student_id = int(input("Enter student ID: "))
                if student_id <= 0:
                    print("Student ID must be a positive integer. Try again.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid integer for student ID.")

        new_student = Student(name, student_id, age, address if address else None)
        self.student_list.append(new_student)
        print(f"--> Added '{name}' successfully.")

    def display_sorted_by_age(self):
        """Sorts students by age in ascending order and displays them."""
        if not self.student_list:
            print("\nNo students to display.")
            return

        # SORTING: Uses Python's sorted() with a lambda key to sort by the 'age' attribute
        sorted_students = sorted(self.student_list, key=lambda student: student.age)

        print("\n" + "=" * 38)
        print("    STUDENT LIST (SORTED BY AGE)    ")
        print("=" * 38)
        for index, student in enumerate(sorted_students, start=1):
            # Invoking the encapsulated method from the Student object
            print(f"{index}. {student.get_info()}")
        print("=" * 38)


def main():
    manager = StudentManager()

    # Outer TRY-EXCEPT to catch runtime interruptions (e.g., KeyboardInterrupt)
    try:
        while True:
            manager.add_student()
            manager.display_sorted_by_age()

            choice = input("\nAdd another student? (y/n): ").strip().lower()
            if choice != 'y':
                print("\nGoodbye!")
                break
    except Exception as error:
        print(f"\nAn unexpected program error occurred: {error}")


if __name__ == "__main__":
    main()