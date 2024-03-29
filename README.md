# Capstone-Project-II---LV1
This is my second project that demonstates my skills as a software engineer.

## Description of the project
1. What is the project
2. How does it work

### What is the project
This project is a software program that is designed to help a small business assign and manage tasks for each member of the business.
This project consists of 3 main files.
1. The main program python file (The other main file is part 2 of the same project)
2. The user text file that has a list of the registered users and their individual passwords
3. The tasks text file that has all the neccessary details of each assigned task.

### How does it work
There are 2 parts to this program.

#### Part 1
The program has a login menu. The program will request the user for their username and password. <br/>
If the username or password is wrong, the username and password will be requested until both are correct.

Once the login is correct, the program will have a menu with the following options:
1. **r - register user**
2. **a - add task**
3. **va - view all tasks**
4. **vm - view my tasks**
5. **e - exit**

The **_register user_** option allows any member to register a new user, along with password, to use the software program.<br/>
The details of the user login crdentials are _stored_ in _user.txt_.

The **_add task_** option allows one to assign a new task to a member of the team along with _when_ the task is assigned and the _deadline_ for task to be completed.
The _details_ of the tasks are stored in _tasks.txt_.

The **_view all tasks_** option allows anyone to see **all** the tasks assigned to which member of the team along with tasks details.

The **_view my tasks_** option allows the user logged in to see **all** their assigned tasks along with tasks details.

The **_exit_** option let's the user log off the software program.

#### Part 2
This part has all the functionalites of the 1st part. The **only 2 differences** are:
1. **Only the admin user** can register users to the software programme.
2. **Only the admin user** can view **statistics** (added as a menu option) that shows **_both_** the _total number of tasks_ assigned and the _total number of users_.
