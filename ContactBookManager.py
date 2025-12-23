class Contact:
    def __init__(self, name, phone, email, category="Other"):
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.category}"


class ContactBook:
    def __init__(self):
        self.contactbook = []

    def add_contact(self, contact):
        self.contactbook.append(contact)
        print(f"Added: {contact.name}")

    def show_all(self):
        if len(self.contactbook) == 0:
            print("No contacts available")
            return

        print("\n=== All contacts ===\n")
        for contact in self.contactbook:
            print(contact)

    def search_by_name(self, name):
        results = []
        for contact in self.contactbook:
            if name.lower() == contact.name.lower():
                results.append(contact)
        return results

    def get_by_category(self, category):
        results = []
        for contact in self.contactbook:
            if contact.category == category:
                results.append(contact)
        return results

    def delete_contact(self, name):
        for contact in self.contactbook:
            if contact.name.lower() == name.lower():
                self.contactbook.remove(contact)
                print(f"Deleted: {name}")
                return

        print(f"Contact '{name}' not found!")


if __name__ == "__main__":
    print("="*50)
    print("CONTACT BOOK - TESTING")
    print("="*50)

    # Create contact book
    book = ContactBook()

    # TEST 1: Add contacts
    print("\n--- TEST 1: Adding Contacts ---")
    book.add_contact(Contact("Alice Smith", "555-1234",
                     "alice@email.com", "Friends"))
    book.add_contact(
        Contact("Bob Johnson", "555-5678", "bob@work.com", "Work"))
    book.add_contact(Contact("Charlie Brown", "555-9012",
                     "charlie@email.com", "Friends"))
    book.add_contact(Contact("Mom", "555-0000", "mom@family.com", "Family"))
    book.add_contact(Contact("Dad", "555-1111", "dad@family.com", "Family"))

    # TEST 2: Show all contacts
    print("\n--- TEST 2: Show All Contacts ---")
    book.show_all()

    # TEST 3: Search by name (exact match)
    print("\n--- TEST 3: Search for 'Alice Smith' ---")
    results = book.search_by_name("Alice Smith")
    if results:
        for contact in results:
            print(f"  Found: {contact}")
    else:
        print("  No results found")

    # TEST 4: Search by name (case insensitive)
    print("\n--- TEST 4: Search for 'alice' (lowercase) ---")
    results = book.search_by_name("alice")
    if results:
        for contact in results:
            print(f"  Found: {contact}")
    else:
        print("  No results found")

    # TEST 5: Search for non-existent contact
    print("\n--- TEST 5: Search for 'John' (doesn't exist) ---")
    results = book.search_by_name("John")
    if results:
        for contact in results:
            print(f"  Found: {contact}")
    else:
        print("  No results found")

    # TEST 6: Get contacts by category (Friends)
    print("\n--- TEST 6: Get 'Friends' Category ---")
    friends = book.get_by_category("Friends")
    print(f"Found {len(friends)} friend(s):")
    for contact in friends:
        print(f"  {contact}")

    # TEST 7: Get contacts by category (Family)
    print("\n--- TEST 7: Get 'Family' Category ---")
    family = book.get_by_category("Family")
    print(f"Found {len(family)} family member(s):")
    for contact in family:
        print(f"  {contact}")

    # TEST 8: Get contacts by category (Work)
    print("\n--- TEST 8: Get 'Work' Category ---")
    work = book.get_by_category("Work")
    print(f"Found {len(work)} work contact(s):")
    for contact in work:
        print(f"  {contact}")

    # TEST 9: Delete existing contact
    print("\n--- TEST 9: Delete 'Bob Johnson' ---")
    book.delete_contact("Bob Johnson")
    print("\nContacts after deletion:")
    book.show_all()

    # TEST 10: Try to delete non-existent contact
    print("\n--- TEST 10: Try to Delete 'John' (doesn't exist) ---")
    book.delete_contact("John")

    # TEST 11: Delete with case insensitive
    print("\n--- TEST 11: Delete 'ALICE SMITH' (uppercase) ---")
    book.delete_contact("ALICE SMITH")
    print("\nContacts after deletion:")
    book.show_all()

    # TEST 12: Show final count
    print("\n--- TEST 12: Final Contact Count ---")
    print(f"Total contacts remaining: {len(book.contactbook)}")

    print("\n" + "="*50)
    print("ALL TESTS COMPLETE! ✅")
    print("="*50)
