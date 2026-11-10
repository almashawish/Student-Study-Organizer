
# Store subjects and tasks
subjects = []
tasks = []

# Add a new subject
def add_subject():
    name = input("Enter subject name: ")

    if name == "":
        print("Subject name cannot be empty.")
    elif name in subjects:
        print("Subject already exists.")
    else:
        subjects.append(name)
        print("Subject added!")


# Show all subjects
def view_subjects():
    if len(subjects) == 0:
        print("No subjects found.")
    else:
        print("\nYour subjects:")
        for i in range(len(subjects)):
            print(i + 1, "-", subjects[i])


# Add a new study task
def add_task():
    if len(subjects) == 0:
        print("Add a subject first.")
    else:
        name = input("Enter task name: ")

        if name == "":
            print("Task name cannot be empty.")
        else:
            view_subjects()

            number = int(input("Choose subject number: "))

            if number >= 1 and number <= len(subjects):
                subject = subjects[number - 1]

                # Each task has a name, subject and status
                task = [name, subject, "Pending"]
                tasks.append(task)

                print("Task added!")
            else:
                print("Invalid subject number.")


# Show all study tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nYour tasks:")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i][0],
                  "| Subject:", tasks[i][1],
                  "| Status:", tasks[i][2])


# Mark a task as completed
def complete_task():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        view_tasks()

        number = int(input("Enter task number: "))

        if number >= 1 and number <= len(tasks):
            tasks[number - 1][2] = "Completed"
            print("Task completed!")
        else:
            print("Invalid task number.")


# Count completed and pending tasks
def show_task_counts():
    completed = 0
    pending = 0

    for task in tasks:
        if task[2] == "Completed":
            completed = completed + 1
        else:
            pending = pending + 1

    print("Completed tasks:", completed)
    print("Pending tasks:", pending)


# Show the main menu
def show_menu():
    print("\n=== Student Study Organizer ===")
    print("1. Add a new subject")
    print("2. View all subjects")
    print("3. Add a study task")
    print("4. View all study tasks")
    print("5. Complete a task")
    print("6. Show task counts")
    print("7. Exit")


# Start the program
def main():
    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_subject()
        elif choice == "2":
            view_subjects()
        elif choice == "3":
            add_task()
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            complete_task()
        elif choice == "6":
            show_task_counts()
        elif choice == "7":
            print("Goodbye! Happy studying!")
            break
        else:
            print("Invalid choice.")


main()
