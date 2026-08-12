# Bundles the title and author details along with formatting logic into a 
# single Book object.
class Book:
    def __init__(self, title: str, author: str):
        self.title = title.strip()      # Attribute
        self.author = author.strip()    # Attribute

    def get_info(self) -> str:
        """Returns a formatted string representation of the book."""
        return f"'{self.title}' by {self.author}"


# Hides list management, search operations, command parsing, and validation 
# behind clean methods in the BookManager class.
class BookManager:
    def __init__(self):
        self.book_list = []  # List holding Book object instances

    def process_command(self, user_input: str):
        """Parses the command string, validates syntax, and routes to actions."""
        cmd_str = user_input.strip()

        if not cmd_str:
            raise ValueError("Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author.")

        # Split command word from the remaining argument
        parts = cmd_str.split(' ', 1)
        action = parts[0].upper()

        if len(parts) < 2 or not parts[1].strip():
            raise ValueError("Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author.")

        param = parts[1].strip()

        if action == "ADD":
            # ADD requires a title and an author separated by a comma
            if ',' not in param:
                raise ValueError("Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author.")

            title, author = param.split(',', 1)
            title = title.strip()
            author = author.strip()

            if not title or not author:
                raise ValueError("Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author.")

            self.add_book(title, author)

        elif action == "REMOVE":
            self.remove_book(param)

        elif action == "SEARCH":
            self.search_book(param)

        else:
            raise ValueError("Invalid input. Please use ADD, REMOVE, or SEARCH followed by the book title and author.")

    def add_book(self, title: str, author: str):
        """Adds a new book if it does not already exist in the list."""
        # Check if book already exists (case-insensitive check)
        for book in self.book_list:
            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                print(f"--> Book '{title}' by {author} already exists in the collection.")
                return

        # OOP CONCEPT: Object Instantiation
        new_book = Book(title, author)
        self.book_list.append(new_book)
        print(f"--> Added book: '{new_book.title}' by {new_book.author}")

    def remove_book(self, title: str):
        """Removes a book by title after verifying its existence."""
        for book in self.book_list:
            if book.title.lower() == title.lower():
                self.book_list.remove(book)
                print(f"--> Removed book: '{book.title}' by {book.author}")
                return

        print(f"--> Cannot remove. Book '{title}' not found in the collection.")

    def search_book(self, title: str):
        """Searches for a book by title."""
        for book in self.book_list:
            if book.title.lower() == title.lower():
                print(f"Book found: {book.title} by {book.author}")
                return

        print("Book not found")

    def display_all_books(self):
        """Displays all books currently stored in the collection."""
        print("\n" + "=" * 45)
        print("          CURRENT BOOK COLLECTION          ")
        print("=" * 45)

        if not self.book_list:
            print("No books in the collection.")
        else:
            for index, book in enumerate(self.book_list, start=1):
                print(f"{index}. {book.get_info()}")

        print("=" * 45)


def main():
    manager = BookManager()

    while True:
        # INNER LOOP: Continues asking until a valid command is entered
        while True:
            user_input = input("\nEnter command (e.g., ADD Hamlet, Shakespeare | REMOVE Hamlet | SEARCH Hamlet): ").strip()

            # TRY-EXCEPT: Catches invalid command formats
            try:
                manager.process_command(user_input)
                break  # Exit inner loop ONLY when command processes successfully
            except ValueError as error:
                print(error)

        # Show the updated collection list after every command
        manager.display_all_books()

        # Prompt for next action only AFTER a successful command
        choice = input("\nPerform another action? (y/n): ").strip().lower()
        if choice != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()