import operations

# Add novels
print(operations.add_book("NOV001", "Things Fall Apart", "Chinua Achebe", "Fiction", 5))
print(operations.add_book("NOV002", "The Alchemist", "Paulo Coelho", "Fiction", 4))
print(operations.add_book("NOV003", "1984", "George Orwell", "Sci-Fi", 5))  # Increased copies to 5 for multiple borrows
print(operations.add_book("NOV004", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 3))  # Added with 3 copies

# Add members with local names
print(operations.add_member(1, "Jeremiah Dave", "jeremiah@local.sl"))
print(operations.add_member(2, "Amadu Coker", "amadu@local.sl"))
print(operations.add_member(3, "Fatima Bangura", "fatima@local.sl"))
print(operations.add_member(4, "Saidu Conteh", "saidu@local.sl"))
print(operations.add_member(5, "Mariama Kamara", "mariama@local.sl"))

# Borrow novels
print(operations.borrow_book("NOV001", 1))  # Success
print(operations.borrow_book("NOV002", 1))  # Success
print(operations.borrow_book("NOV003", 1))  # Success
print(operations.borrow_book("NOV004", 1))  # Success - now with NOV004 added, no error
print(operations.borrow_book("NOV003", 1))  # Fail: Limit (after 4 borrows, but limit is 3, so this is the 4th)
print(operations.borrow_book("NOV005", 1))  # Fail: Not found
operations.update_book("NOV004", total_copies=0)
print(operations.borrow_book("NOV004", 2))  # Fail: No copies, but since borrowed already by 1, but update to 0 after borrow

# Search novels
print(operations.search_book("Things"))
print(operations.search_book("Alchemist"))
print(operations.search_book(""))  # Fail: Empty

# Update novel
print(operations.update_book("NOV001", title="Things Fall Apart Updated", total_copies=6))
print(operations.update_book("NOV001", genre="Mystery"))  # Fail: Invalid genre
print(operations.update_book("NOV005", title="Missing"))  # Fail: Not found

# Return novel
print(operations.return_book("NOV001", 1))  # Success
print(operations.return_book("NOV005", 1))  # Fail: Not borrowed

# Delete novel
print(operations.delete_book("NOV001"))  # Success
print(operations.delete_book("NOV002"))  # Fail: Borrowed

# Extra borrow with other member
print(operations.borrow_book("NOV004", 3))  # Success for Fatima, but total_copies=0 after update, so fail if not borrowed before