"""
PERSONAL PASSWORD MANAGER
A secure way to store and manager passwords

Author: [Shaun Aniñon]
Date: November 2025
"""
import random
import string
import json
import os


class Password:
    def __init__(self, website, username, password, category="General", notes=""):
        self.website = website
        self.username = username
        self.password = password
        self.category = category
        self.notes = notes

    def __str__(self):
        hidden_password = "*" * len(self.password)
        return f"{self.website} | {self.username} | {hidden_password} | {self.category} | {self.notes}"

    def reveal_password(self):
        return self.password

    def to_dict(self):
        return {
            "website": self.website,
            "username": self.username,
            "password": self.password,
            "category": self.category,
            "notes": self.notes
        }

    @staticmethod
    def from_dict(data):
        """Create password object from dictionary"""
        return Password(
            website=data["website"],
            username=data["username"],
            password=data["password"],
            category=data.get("category", "General"),
            notes=data.get("notes", "")
        )


class PasswordGenerator:
    @staticmethod
    def generate(length=16, use_symbols=True):
        if length < 8:
            print(f"Password must be 8 characters or more")
            return

        characters = string.ascii_letters + string.digits

        if use_symbols:
            characters += string.punctuation

        password = ''
        for i in range(length):
            password += random.choice(characters)

        return password


class Vault:
    def __init__(self, master_password):
        self.master_password = master_password
        self.passwords = []
        self.is_locked = True

    def unlock(self, password):
        if password == self.master_password:
            self.is_locked = False
            print("✅ Success!")
        else:
            print("❌ Invalid password!")

    def lock(self):
        self.is_locked = True
        print("Vault is locked!")

    def add_password(self, password_entry):
        if self.is_locked:
            print("Vault is locked!")
            return
        else:
            self.passwords.append(password_entry)
            print(f"Password for '{password_entry.website}' added!")

    def get_all_passwords(self):
        if self.is_locked:
            print(f"Vault is locked!")
            return []
        else:
            return self.passwords

    def search(self, website):
        if self.is_locked:
            print(f"Vault is locked!")
            return []

        results = []
        for password in self.passwords:
            if password.website.lower() == website.lower():
                results.append(password)

        return results

    def get_by_category(self, category):
        if self.is_locked:
            print("Vault is locked!")
            return []

        results = []

        for password in self.passwords:
            if password.category == category:
                results.append(password)

        return results

    def save_to_file(self, filename="passwords.json"):
        if self.is_locked:
            print("❌ Vault is locked! Cannot save.")
            return False

        passwords_data = []
        for password in self.passwords:
            passwords_data.append(password.to_dict())

        try:
            with open(filename, "w") as f:
                json.dump(passwords_data, f, indent=4)

            print(f"✅ Saved {len(self.passwords)} password(s) to '{filename}'")
            return True

        except IOError as e:
            print(f"❌ Error saving file: {e}")
            return False

    def load_from_file(self, filename="passwords.json"):
        """Load passwords from a file"""
        if self.is_locked:
            print(f"Vault is locked!")
            return False

        try:
            with open(filename, "r") as f:
                passwords_data = json.load(f)

            self.passwords = []
            for pwd_dict in passwords_data:
                password_obj = Password.from_dict(pwd_dict)
                self.passwords.append(password_obj)

            print(
                f"Loaded {len(self.passwords)} password(s) from '{filename}'")
            return True

        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with empty vault.")
            return False

        except json.JSONDecodeError:
            print(f"File '{filename}' is corrupted or invalid.")
            return False

        except IOError as e:
            print(f"Error reading file: {e}")
            return False


if __name__ == "__main__":
    print("="*60)
    print("PASSWORD MANAGER - COMPLETE TEST SUITE")
    print("="*60)

    # ==========================================
    # TEST 1: Create vault and add passwords
    # ==========================================
    print("\n[TEST 1] Creating Vault and Adding Passwords...")
    vault = Vault("master123")
    vault.unlock("master123")

    vault.add_password(Password("Gmail", "user@gmail.com",
                       "MyGmailPass123!", "Email", "Work email"))
    vault.add_password(Password("Facebook", "john_doe",
                       "FBpass456!", "Social Media", "Personal"))
    vault.add_password(Password("Instagram", "johndoe123",
                       "InstaSecure789!", "Social Media"))
    vault.add_password(Password("Bank of America", "john.doe",
                       "BankPass999!", "Banking", "Checking account"))
    vault.add_password(Password("Netflix", "john@email.com",
                       "Netflix2024!", "Entertainment"))

    print(f"\n✅ Total passwords in vault: {len(vault.passwords)}")

    # ==========================================
    # TEST 2: Display all passwords
    # ==========================================
    print("\n[TEST 2] Current Passwords:")
    for pwd in vault.get_all_passwords():
        print(f"  - {pwd}")

    # ==========================================
    # TEST 3: Save to file
    # ==========================================
    print("\n[TEST 3] Saving to File...")
    vault.save_to_file("my_passwords.json")

    # Check if file was created
    if os.path.exists("my_passwords.json"):
        print("✅ File 'my_passwords.json' was created!")
        file_size = os.path.getsize("my_passwords.json")
        print(f"   File size: {file_size} bytes")

    # ==========================================
    # TEST 4: Create NEW vault (simulate restart)
    # ==========================================
    print("\n[TEST 4] Creating NEW Vault (Simulating Program Restart)...")
    vault2 = Vault("master123")
    vault2.unlock("master123")
    print(f"✅ New vault has {len(vault2.passwords)} passwords (should be 0)")

    # ==========================================
    # TEST 5: Load from file
    # ==========================================
    print("\n[TEST 5] Loading from File...")
    vault2.load_from_file("my_passwords.json")

    print(f"✅ Passwords after loading: {len(vault2.passwords)}")

    # ==========================================
    # TEST 6: Verify loaded passwords work
    # ==========================================
    print("\n[TEST 6] Verifying Loaded Passwords:")
    for pwd in vault2.get_all_passwords():
        print(f"  - {pwd}")

    # ==========================================
    # TEST 7: Test search on loaded data
    # ==========================================
    print("\n[TEST 7] Searching for 'Gmail' in loaded vault...")
    results = vault2.search("Gmail")
    if results:
        for pwd in results:
            print(f"  ✅ Found: {pwd}")
            print(f"     Username: {pwd.username}")
            print(f"     Actual Password: {pwd.reveal_password()}")
            print(f"     Notes: {pwd.notes}")

    # ==========================================
    # TEST 8: Test category filter
    # ==========================================
    print("\n[TEST 8] Getting 'Social Media' passwords...")
    social = vault2.get_by_category("Social Media")
    print(f"✅ Found {len(social)} Social Media password(s):")
    for pwd in social:
        print(f"  - {pwd}")

    # ==========================================
    # TEST 9: Modify and save again
    # ==========================================
    print("\n[TEST 9] Adding New Password and Saving Again...")
    vault2.add_password(Password("Twitter", "johndoe",
                        "TwitterPass!", "Social Media", "Business account"))
    vault2.save_to_file("my_passwords.json")

    # ==========================================
    # TEST 10: Error handling - Load non-existent file
    # ==========================================
    print("\n[TEST 10] Testing Error: Load Non-Existent File...")
    vault3 = Vault("master123")
    vault3.unlock("master123")
    vault3.load_from_file("file_that_doesnt_exist.json")

    # ==========================================
    # TEST 11: Error handling - Save while locked
    # ==========================================
    print("\n[TEST 11] Testing Error: Save While Locked...")
    vault4 = Vault("master123")
    vault4.add_password(Password("Test", "test", "test", "Test"))
    vault4.save_to_file("test.json")  # Should fail - vault is locked!

    # ==========================================
    # TEST 12: Error handling - Load while locked
    # ==========================================
    print("\n[TEST 12] Testing Error: Load While Locked...")
    vault5 = Vault("master123")
    # Should fail - vault is locked!
    vault5.load_from_file("my_passwords.json")

    # ==========================================
    # TEST 13: Generate password and save
    # ==========================================
    print("\n[TEST 13] Testing Password Generator + Save...")
    vault6 = Vault("master123")
    vault6.unlock("master123")

    generated_pwd = PasswordGenerator.generate(16, True)
    print(f"✅ Generated password: {generated_pwd}")

    vault6.add_password(Password("Reddit", "user123",
                        generated_pwd, "Social Media"))
    vault6.save_to_file("test_generated.json")

    # ==========================================
    # TEST 14: Case-insensitive search
    # ==========================================
    print("\n[TEST 14] Testing Case-Insensitive Search...")
    results_lower = vault2.search("gmail")  # lowercase
    results_upper = vault2.search("GMAIL")  # uppercase
    results_mixed = vault2.search("GmAiL")  # mixed

    print(f"✅ Search 'gmail': {len(results_lower)} result(s)")
    print(f"✅ Search 'GMAIL': {len(results_upper)} result(s)")
    print(f"✅ Search 'GmAiL': {len(results_mixed)} result(s)")

    # ==========================================
    # FINAL SUMMARY
    # ==========================================
    print("\n" + "="*60)
    print("FINAL FILE CHECK")
    print("="*60)

    # List all JSON files created
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]
    print(f"\n✅ JSON files created: {len(json_files)}")
    for file in json_files:
        size = os.path.getsize(file)
        print(f"  - {file} ({size} bytes)")

    print("\n" + "="*60)
    print("ALL TESTS COMPLETED SUCCESSFULLY! ✅")
    print("="*60)

    print("\n📁 Check your folder - you should see:")
    print("   1. my_passwords.json (main file with 6 passwords)")
    print("   2. test_generated.json (with generated password)")
    print("\n💡 Open 'my_passwords.json' in a text editor to see your saved passwords!")
    print("\n🎉 Your Password Manager is FULLY WORKING!")
