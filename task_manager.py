# The program is for a small business.
# It will manage tasks and assign task to each member of the team.

# Date today import
from datetime import date

# Empty list variables
task_output = []
user_output = []

# Empty variables
user_setlist = ""
pass_input = ""
message = ""

# User List
# Read the user.txt file
with open("user.txt", "r") as user_pass_list:
    for user_line in user_pass_list:
        user_line_strip = user_line.strip()
        user_output.append(user_line_strip)
        user_setlist = user_output

    # LOGIN CODE
    # We read username and password from file
    # Enter username.
    # If wrong username is given, and error message will print
    user_input = input("Please enter username: ")

    # We set the False value to Login variable
    login = False

    # FOR loop to read list items
    for j in user_setlist:
        split_j = j.split(", ")
        if user_input == split_j[0]:
            login = True
            break

    # While loop conditions for login
    while not login:
        print("Wrong username. Try again.")
        user_input = input("Please enter username: ")
        for j in user_setlist:
            split_j = j.split(", ")
            if user_input == split_j[0]:
                login = True
                break

    # Enter password.
    # If wrong password is given, and error message will print
    if user_input == split_j[0]:
        pass_input = input("Please enter password: ")
        while pass_input != split_j[1]:
            print("Wrong password. Try again.")
            pass_input = input("Please enter password: ")

# If the username and password is right, the menu will display.
if user_input == split_j[0] and pass_input == split_j[1]:
    option_sentence = input("Please select one of the following: \n"
                            "r - register task\n"
                            "a - add task\n"
                            "va - view all tasks\n"
                            "vm - view my tasks\n"
                            "e - exit\n"
                            "Enter your choice: \t")

    # List that checks for right input
    keyword_list = ["r", "a", "va", "vm", "e"]
    # Used to check if the right input is given
    for x in keyword_list:
        if x == option_sentence:
            message = option_sentence

    # Loops code until we receive the right input
    while option_sentence != message:
        option_sentence = input("Please select one of the following: \n"
                                "r - register task\n"
                                "a - add task\n"
                                "va - view all tasks\n"
                                "vm - view my tasks\n"
                                "e - exit\n"
                                "Enter your choice: \t")

        # Used to check if the right input is given
        for x in keyword_list:
            if x == option_sentence:
                message = option_sentence

# We add new users and their passwords
if message == "r":
    # Added new users and their passwords depending on the number of new users
    num_user = int(input("What is the number of input users? "))

    # We append the following details into tasks.txt and format it.
    with open("user.txt", "a") as f:
        new_user_input = input("Please enter new username: ")
        user_name = new_user_input
        new_pass_input = input("Please enter new password: ")
        new_pass_input2 = input("Please enter new password again: ")
        if new_pass_input != new_pass_input2:
            print("Passwords do not match")
            while new_pass_input != new_pass_input2:
                new_pass_input = input("Please enter new password: ")
                new_pass_input2 = input("Please enter new password again: ")

        if new_pass_input == new_pass_input2:
            password = new_pass_input

        user_password = f"{user_name}, {password}"
        f.write(f"\n{user_password}\n")

# Add Tasks to tasks.txt
elif message == "a":
    # Add tasks based on number of task inputs.
    num_task = int(input("Number of tasks to be assigned? "))

    # We append the following details into tasks.txt and format it.
    with open("tasks.txt", "a") as add_task:
        user_task = input("Who is the task assigned to? ")
        title_task = input("Title of the task? ")
        description_task = input("Description of the task? ")
        today = ""
        date_assign_task = str(date.today())
        date_due_task = input("When is the task due? ")
        completed_task = "No"
        task_assignment = f"{user_task}, {title_task}, " \
                          f"{description_task}, {date_assign_task}, " \
                          f"{date_due_task}, {completed_task}"
        add_task.write(f"\n{task_assignment}\n")

# View all tasks in tasks.txt
elif message == "va":

    # We read from the tasks.txt
    with open("tasks.txt", "r") as user_task_list:
        for task_line in user_task_list:
            task_line_strip = task_line.strip()
            task_output.append(task_line_strip)

    # FOR loop to put into task stringed list
    for i in task_output:
        # Turns i into a list format
        all_list_split = i.split(", ")

        # Prints all task details of the tasks.txt
        print("\n")
        print(f"Task: {all_list_split[1]}")
        print(f"Assigned to: {all_list_split[0]}")
        print(f"Date assigned: {all_list_split[3]}")
        print(f"Due date: {all_list_split[4]}")
        print(f"Task complete: {all_list_split[5]}")
        print(f"Task Description: {all_list_split[2]}")

# View my tasks option
elif message == "vm":

    # We read from the tasks.txt
    with open("tasks.txt", "r") as user_task_list:
        for task_line in user_task_list:
            task_line_strip = task_line.strip()
            task_output.append(task_line_strip)

    # FOR loop to put into task stringed list
    for i in task_output:
        # Looks for line that begins with user_input
        if i.startswith(f"{user_input}"):
            # Turns i into a list format
            my_list_split = i.split(", ")

            # Prints all task details of the user
            print("\n")
            print(f"Task: {my_list_split[1]}")
            print(f"Assigned to: {my_list_split[0]}")
            print(f"Date assigned: {my_list_split[3]}")
            print(f"Due date: {my_list_split[4]}")
            print(f"Task complete: {my_list_split[5]}")
            print(f"Task Description: {my_list_split[2]}")
        # Prints if there are no task assignments

# Exits the program
elif message == "e":
    print("You have exited the program.")


# Reference
# https://www.programiz.com/python-programming/methods/string

# https://www.daniweb.com/programming/software-development  \
# /threads/317757/print-lines-that-start-with-a-specific-word
