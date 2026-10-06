books = (["The Alchemist" , "1984" , "Moby Dick" , "Pride and Prejudice"])

books.append("Harry Potter")
books.append("Hobbit")

books.remove("1984")

books.sort()
print(books)

borrower = ("John Doe" , "B1023" , "2025-10-15")

try:
    borrower[0] = "Jane Doe"
except TypeError as e:
    print(f"Error: {e}")

print(f"Length of borrower tuple: {len(borrower)}")

for detail in borrower:
    print(f"- {detail}")


book_info = ("The Alchemist", "Paulo Coelho", 1988)

book_title, author , year = book_info

print(f"Book Title: {book_title}")

print(f"Author: {author}")

print(f"Year Published: {year}")


borrowed_books = [23,19,31,27,22,30,25]

week_2_to_5 = borrowed_books[1:5]

borrowed_books[0] = 20
print(f"Updated borrowed books list: {borrowed_books}")
print(f"Books borrowed from week 2 to week 5: {week_2_to_5}")