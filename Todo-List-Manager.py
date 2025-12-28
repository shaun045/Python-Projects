class TodoItem:
    def __init__(self, task):
        self.task = task
        self.completed = False

    def __str__(self):
        status = "[X]" if self.completed else "[]"
        return f"{status} {self.task}"

    def mark_complete(self):
        self.completed = True


class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, task):
        todo = TodoItem(task)
        self.items.append(todo)

    def show_all(self):
        if len(self.items) == 0:
            print("No tasks available")
            return

        print("\n=== All Todos ===\n")
        for item in self.items:
            print(item)

    def show_incomplete(self):
        print("\n=== Incomplete Todos ===\n")

        incomplete = []
        for item in self.items:
            if not item.completed:
                incomplete.append(item)

        if len(incomplete) == 0:
            print("All task completed! No incomplete tasks left!")
            return

        for item in incomplete:
            print(item)

    def mark_item_complete(self, index):
        if 0 <= index < len(self.items):
            self.items[index].mark_complete()
            print(f"Completed: {self.items[index].task}")
        else:
            print("Invalid todo number!")

    def show_complete(self):
        print("\n=== Completed Todos ===\n")
        completed = []
        for item in self.items:
            if item.completed:
                completed.append(item)

        if len(completed) == 0:
            print("No completed todos yet!")
            return

        for i, item in enumerate(completed, start=1):
            print(f"{i}. {item}")
        print()


if __name__ == "__main__":
    print("="*50)
    print("TODO LIST MANAGER")
    print("="*50)

    # Create todo list
    todos = TodoList()

    # Add some todos
    print("\n--- Adding Todos ---")
    todos.add_item("Buy groceries")
    todos.add_item("Learn Python")
    todos.add_item("Build a project")
    todos.add_item("Exercise")
    todos.add_item("Read a book")

    # Show all
    todos.show_all()

    # Mark some as complete
    print("--- Marking Some Complete ---")
    todos.mark_item_complete(0)  # Buy groceries
    todos.mark_item_complete(2)  # Build a project

    # Show all again
    todos.show_all()

    # Show only incomplete
    todos.show_incomplete()

    # Show only complete
    todos.show_complete()

    print("="*50)
    print("TEST COMPLETE! ✅")
    print("="*50)
