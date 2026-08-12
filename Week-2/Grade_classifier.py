# Bundles an individual student's score with the comparison logic required 
# to calculate its corresponding letter grade.
class StudentScore:
    def __init__(self, score: float):
        self.score = score  # Attribute

    def get_grade(self) -> str:
        """Determines letter grade using comparison operators in conditional statements."""
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'



# Hides string parsing, iteration loops, score validation, and formatting 
# behind clean methods in the GradeClassifier class.
class GradeClassifier:
    def __init__(self):
        self.score_list = []  # List to store StudentScore object instances

    def process_scores(self, raw_input: str):
        """Parses input format like '[90, 85.5, 72]' into a list of StudentScore objects."""
        text = raw_input.strip()

        # Check for and strip outer square brackets
        if text.startswith('[') and text.endswith(']'):
            text = text[1:-1]
        else:
            raise ValueError()

        if not text.strip():
            raise ValueError()

        # Split input string by commas into individual score strings
        raw_scores = text.split(',')
        temp_list = []

        # LOOP: Iterate over score items, parse, and validate each value
        for item in raw_scores:
            clean_item = item.strip()
            if not clean_item:
                continue

            score = float(clean_item)  # Raises ValueError if non-numeric
            
            # Range check for valid scores (0 to 100)
            if score < 0 or score > 100:
                raise ValueError()

            # OOP CONCEPT: Object Instantiation
            temp_list.append(StudentScore(score))

        if not temp_list:
            raise ValueError()

        self.score_list = temp_list

    def display_grades(self):
        """Iterates over the list of scores and displays each formatted grade."""
        print("\n" + "=" * 45)
        print("             STUDENT GRADE REPORT            ")
        print("=" * 45)

        # LOOP: Iterate through the list of StudentScore objects
        for index, student in enumerate(self.score_list, start=1):
            # Keeps 1 place after decimal point (.1f)
            print(f"Student #{index}: Score = {student.score:.1f} | Grade = {student.get_grade()}")

        print("=" * 45)


def main():
    classifier = GradeClassifier()

    while True:
        # INNER LOOP: Continues asking until valid input in correct format is provided
        while True:
            user_input = input("\nEnter scores (format: [score1, score2, ...]): ").strip()

            # TRY-EXCEPT: Catches formatting, non-numeric, and range errors
            try:
                classifier.process_scores(user_input)
                classifier.display_grades()
                break  # Exit inner loop ONLY when score parsing succeeds
            except ValueError:
                print("Invalid input. Please enter the scores with correct format, e.g., [90, 85.5, 72, 58].")

        # Prompt for next batch only AFTER a valid list is processed
        choice = input("\nProcess another list of scores? (y/n): ").strip().lower()
        if choice != 'y':
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()