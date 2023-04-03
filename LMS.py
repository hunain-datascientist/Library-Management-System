# Create an empty dictionary to store books
library = {}

# Function to add a book to the library
def add_book():
    book_name = input("Enter the name of the book: ")
    author_name = input("Enter the name of the author: ")
    publication_year = input("Enter the publication year: ")
    library[book_name] = {"Author": author_name, "Publication Year": publication_year}
    print("Book added successfully!\n")

# Function to remove a book from the library
def remove_book():
    book_name = input("Enter the name of the book: ")
    if book_name in library:
        del library[book_name]
        print("Book removed successfully!\n")
    else:
        print("Book not found.\n")

# Function to search for a book in the library
def search_book():
    book_name = input("Enter the name of the book: ")
    if book_name in library:
        print("Book found!\n")
        print("Book Name:", book_name)
        print("Author:", library[book_name]["Author"])
        print("Publication Year:", library[book_name]["Publication Year"])
    else:
        print("Book not found.\n")
# Function to borrow a book from the library
def borrow_book():
    book_name = input("Enter the name of the book you want to borrow: ")
    if book_name in library:
        if "Borrower" not in library[book_name]:
            borrower_name = input("Enter your name: ")
            library[book_name]["Borrower"] = borrower_name
            print(f"{book_name} borrowed successfully by {borrower_name}.\n")
        else:
            print(f"{book_name} is already borrowed by {library[book_name]['Borrower']}.\n")
    else:
        print("Book not found.\n")
# Function to return a book to the library
def return_book():
    book_name = input("Enter the name of the book you want to return: ")
    if book_name in library:
        if "Borrower" in library[book_name]:
            borrower_name = library[book_name]["Borrower"]
            del library[book_name]["Borrower"]
            print(f"{book_name} returned successfully by {borrower_name}.\n")
        else:
            print(f"{book_name} is not currently borrowed.\n")
    else:
        print("Book not found.\n")
# Function to display all the books in the library
def display_books():
    if len(library) == 0:
        print("Library is empty.\n")
    else:
        print("Books in the library:\n")
        for book_name in library:
            print("Book Name:", book_name)
            print("Author:", library[book_name]["Author"])
            print("Publication Year:", library[book_name]["Publication Year"])
            print()

# Main function to run the program
def main():
    while True:
        print("Select an option:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Quit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            borrow_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            print("Thank you for using the library management system.")
            202
        else:
            print("Invalid choice. Please enter a valid choice.\n")
# Call the main function to run the program
main()