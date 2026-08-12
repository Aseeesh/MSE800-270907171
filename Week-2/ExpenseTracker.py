# Bundles a category's name and its list of expense entries together with 
# calculation logic (total, average) into a single object.
class ExpenseCategory:
    def __init__(self, name: str):
        self.name = name
        self.expenses = []  # List storing numeric expense amounts

    def add_expense(self, amount: float):
        """Adds an expense amount to this category's list."""
        self.expenses.append(amount)

    def get_total(self) -> float:
        """Calculates total expenses for this category."""
        return sum(self.expenses)

    def get_average(self) -> float:
        """Calculates average expense for this category."""
        if not self.expenses:
            return 0.0
        return sum(self.expenses) / len(self.expenses)



# Hides dictionary operations, command parsing, category verification, and 
# mathematical aggregations behind clear, high-level methods.
class ExpenseTracker:
    # Predefined categories allowed by the system
    PREDEFINED_CATEGORIES = ['Food', 'Utilities', 'Entertainment', 'Transportation', 'Healthcare']

    def __init__(self):
        # Dictionary mapping category names to ExpenseCategory object instances
        self.categories = {
            category: ExpenseCategory(category) for category in self.PREDEFINED_CATEGORIES
        }

    def process_command(self, user_input: str):
        """Parses raw user input, validates structure, and routes commands."""
        cmd_str = user_input.strip()

        if not cmd_str:
            raise ValueError("Invalid input. Command cannot be empty.")

        parts = cmd_str.split(' ', 1)
        action = parts[0].upper()

        if action in ("REPORT", "SUMMARY"):
            return  # Main report prints automatically after processing

        elif action == "ADD":
            if len(parts) < 2 or ',' not in parts[1]:
                raise ValueError("Invalid format. Use: ADD category, amount (e.g., ADD Food, 25.50)")

            category_part, amount_part = parts[1].split(',', 1)
            category_name = category_part.strip()

            # Input validation: Ensure category is predefined
            matched_category = self._validate_category(category_name)

            # TRY-EXCEPT validation: Ensure expense amount is numeric and positive
            try:
                amount = float(amount_part.strip())
                if amount <= 0:
                    raise ValueError()
            except ValueError:
                raise ValueError("Invalid amount. Expense must be a positive number.")

            # Add expense to the encapsulated category instance
            self.categories[matched_category].add_expense(amount)
            print(f"--> Successfully added ${amount:.2f} to '{matched_category}'.")

        elif action == "TOTAL":
            if len(parts) < 2 or not parts[1].strip():
                raise ValueError("Invalid format. Use: TOTAL category (e.g., TOTAL Food)")

            category_name = parts[1].strip()
            matched_category = self._validate_category(category_name)

            cat_obj = self.categories[matched_category]
            print(f"\n--> Total expenses for '{matched_category}': ${cat_obj.get_total():.2f}")

        else:
            raise ValueError("Invalid command. Please use ADD, TOTAL, or REPORT.")

    def _validate_category(self, category_name: str) -> str:
        """Helper method to verify if a category is defined (case-insensitive)."""
        for category in self.PREDEFINED_CATEGORIES:
            if category.lower() == category_name.lower():
                return category

        allowed_list = ", ".join(self.PREDEFINED_CATEGORIES)
        raise ValueError(f"Invalid category '{category_name}'. Allowed categories: {allowed_list}")

    def display_all_reports(self):
        """Displays total and average expenses across all predefined categories."""
        print("\n" + "=" * 60)
        print("          MONTHLY EXPENSE SUMMARY (TOTAL & AVERAGE)        ")
        print("=" * 60)
        print(f"{'Category':<16} | {'Entries':<8} | {'Total ($)':<12} | {'Average ($)':<12}")
        print("-" * 60)

        grand_total = 0.0

        for category_name, cat_obj in self.categories.items():
            total = cat_obj.get_total()
            avg = cat_obj.get_average()
            count = len(cat_obj.expenses)
            grand_total += total
            print(f"{category_name:<16} | {count:<8} | ${total:<11.2f} | ${avg:<11.2f}")

        print("=" * 60)
        print(f"GRAND TOTAL EXPENSES: ${grand_total:.2f}")
        print("=" * 60)


def main():
    tracker = ExpenseTracker()

    while True:
        # INNER LOOP: Continues prompting until a valid command is executed
        while True:
            print("\nAvailable Categories: Food, Utilities, Entertainment, Transportation, Healthcare")
            user_input = input("Enter command (e.g., ADD Food, 25.50 | TOTAL Food | REPORT): ").strip()

            # TRY-EXCEPT: Catches command errors, bad categories, or invalid numbers
            try:
                tracker.process_command(user_input)
                break  # Exit inner loop ONLY when command is processed successfully
            except ValueError as error:
                print(f"Error: {error}")

        # Show updated expense summary report after every valid command
        tracker.display_all_reports()

        # Prompt for next action ONLY after a successful command execution
        choice = input("\nPerform another action? (y/n): ").strip().lower()
        if choice != 'y':
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()