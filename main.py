# Lists store subjects and study tasks while the program is running.
subjects = []
tasks = []


def add_subject():
    subject_name = input("Enter the subject name: ").strip()

    if subject_name == "":
        print("Subject name cannot be empty.")
    elif subject_name in subjects:
        print("This subject already exists.")
    else:
        subjects.append(subject_name)
        print("Subject added successfully!")


def view_subjects():
    if len(subjects) == 0:
        print("No subjects added yet.")
    else:
        print("\nYour subjects:")
        subject_number = 1
        for subject in subjects:
            print(str(subject_number) + ". " + subject)
            subject_number = subject_number + 1


def add_task():
    if len(subjects) == 0:
        print("Please add a subject first.")
        return

    task_name = input("Enter the task name: ").strip()
    if task_name == "":
        print("Task name cannot be empty.")
        return

    view_subjects()
    subject_choice = input("Choose a subject number: ").strip()

    # Check that the input contains only digits before converting it.
    if not subject_choice.isdigit():
        print("Invalid subject number. Please enter a number from the list.")
        return

    subject_number = int(subject_choice)
    if subject_number < 1 or subject_number > len(subjects):
        print("Invalid subject number. Please enter a number from the list.")
        return

    subject_name = subjects[subject_number - 1]
    task = [task_name, subject_name, "Pending"]
    tasks.append(task)
    print("Study task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No study tasks added yet.")
    else:
        print("\nYour study tasks:")
        task_number = 1
        for task in tasks:
            print(str(task_number) + ". " + task[0] + " | Subject: " + task[1] + " | Status: " + task[2])
            task_number = task_number + 1


def complete_task():
    if len(tasks) == 0:
        print("No study tasks to complete yet.")
        return

    view_tasks()
    task_choice = input("Enter the number of the completed task: ").strip()

    if not task_choice.isdigit():
        print("Invalid task number. Please enter a number from the list.")
        return

    task_number = int(task_choice)
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number. Please enter a number from the list.")
    elif tasks[task_number - 1][2] == "Completed":
        print("This task is already completed.")
    else:
        tasks[task_number - 1][2] = "Completed"
        print("Task marked as completed!")


def show_task_counts():
    completed_count = 0
    pending_count = 0

    for task in tasks:
        if task[2] == "Completed":
            completed_count = completed_count + 1
        else:
            pending_count = pending_count + 1

    print("Completed tasks: " + str(completed_count))
    print("Pending tasks: " + str(pending_count))


def show_menu():
    print("\n=== Student Study Organizer ===")
    print("1. Add a new subject")
    print("2. View all subjects")
    print("3. Add a study task")
    print("4. View all study tasks")
    print("5. Mark a task as completed")
    print("6. Show completed and pending task counts")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

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
            print("Invalid option. Please enter a number from 1 to 7.")


main()
