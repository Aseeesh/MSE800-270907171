# Bundles data fields (name, ID, age, address) and methods into a single class.
class Student:
    def __init__(self, name: str, student_id: str, age: int, address: str):
        self.name = name          # Attribute
        self.student_id = student_id  # Attribute
        self.age = age            # Attribute
        self.address = address    # Attribute

  # this function returns the formatted student details
    def get_info(self) -> str:
        """Returns formatted student details."""
        return f"ID: {self.student_id:<8} | Name: {self.name:<15} | Age: {self.age:<3} | Address: {self.address}"


# Hides list management, sorting details, and input validation from main().
class StudentManager:
    def __init__(self):
        self.student_list = []  # List holding Student object instances

    # this function adds a new student to the list after validating inputs
    def add_student(self):
        print("\n--- Enter Student Details ---")
        name = input("Enter student name: ").strip()
        student_id = input("Enter student ID: ").strip()

        # TRY-EXCEPT: Prevents crashes from invalid age inputs
        while True:
            try:
                age = int(input("Enter student age: "))
                if age <= 0:
                    print("Age must be greater than 0. Try again.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid number for age.")

        address = input("Enter student address: ").strip()

        # OOP CONCEPT: Object Instantiation
        new_student = Student(name, student_id, age, address)
        self.student_list.append(new_student)
        print(f"--> Added '{name}' successfully.")

    def display_sorted_by_age(self):
        """Sorts students by age (ascending) and displays the updated list."""
        if not self.student_list:
            print("\nNo students to display.")
            return

        # SORTING: Lambda extracts the 'age' property from each Student object
        sorted_students = sorted(self.student_list, key=lambda student: student.age)

        print("\n" + "=" * 65)
        print("           CURRENT STUDENT LIST (SORTED BY AGE)")
        print("=" * 65)
        for index, student in enumerate(sorted_students, start=1):
            print(f"{index}. {student.get_info()}")
        print("=" * 65)


def main():
    manager = StudentManager()

    # Outer TRY-EXCEPT to catch runtime interrupts safely
    try:
        while True:
            manager.add_student()
            manager.display_sorted_by_age()

            choice = input("\nAdd another student? (y/n): ").strip().lower()
            if choice != 'y':
                print("\nGoodbye!")
                break
    except Exception as error:
        print(f"\nAn unexpected error occurred: {error}")


if __name__ == "__main__":
    main()