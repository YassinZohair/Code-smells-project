"""
Library Book Manager
---------------------
Models a single library book: its info, borrowing state, fines, and
notification history.

YOUR TASK: This script works correctly, but the LibraryBook class has grown
into a "Large Class" — it's doing several unrelated jobs at once. Refactor
it by splitting responsibilities into separate, cohesive classes. Keep the
same overall behavior (same printed output when you run the script).

Hint: look for methods that never touch the same fields as other methods —
that's a strong clue about where the class boundaries should be.
"""


class LibraryBook:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower_name = None
        self.days_borrowed = 0
        self.notification_log = []

    # --- borrowing state ---
    def borrow(self, borrower_name):
        if self.is_borrowed:
            print(f"Cannot borrow '{self.title}': already borrowed")
            return
        self.is_borrowed = True
        self.borrower_name = borrower_name
        self.days_borrowed = 0
        print(f"'{self.title}' borrowed by {borrower_name}")

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed")
            return
        print(f"'{self.title}' returned by {self.borrower_name}")
        self.is_borrowed = False
        self.borrower_name = None

    def advance_day(self):
        if self.is_borrowed:
            self.days_borrowed += 1

    # --- fine calculation ---
    def calculate_fine(self):
        free_days = 14
        fine_per_day = 0.25
        if self.days_borrowed <= free_days:
            return 0.0
        overdue_days = self.days_borrowed - free_days
        return round(overdue_days * fine_per_day, 2)

    def is_overdue(self):
        return self.days_borrowed > 14

    # --- notifications ---
    def send_due_soon_notice(self):
        message = f"Reminder: '{self.title}' is due soon"
        self.notification_log.append(message)
        print(f"Notifying {self.borrower_name}: {message}")

    def send_overdue_notice(self):
        fine = self.calculate_fine()
        message = f"Overdue: '{self.title}' — current fine ${fine}"
        self.notification_log.append(message)
        print(f"Notifying {self.borrower_name}: {message}")

    # --- catalog / reporting ---
    def print_catalog_entry(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"[{self.isbn}] {self.title} by {self.author} — {status}")

    def print_full_report(self):
        print(f"--- Report for '{self.title}' ---")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {'Borrowed' if self.is_borrowed else 'Available'}")
        if self.is_borrowed:
            print(f"Borrower: {self.borrower_name}")
            print(f"Days borrowed: {self.days_borrowed}")
            print(f"Current fine: ${self.calculate_fine()}")
        print(f"Notifications sent: {len(self.notification_log)}")


if __name__ == "__main__":
    book = LibraryBook("Clean Code", "Robert C. Martin", "978-0132350884")
    book.print_catalog_entry()

    book.borrow("Yassin")
    for _ in range(20):
        book.advance_day()

    if book.is_overdue():
        book.send_overdue_notice()

    book.print_full_report()
    book.return_book()