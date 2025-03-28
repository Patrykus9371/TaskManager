# Task Manager CLI
![image](https://github.com/user-attachments/assets/79da2d84-88b1-4d38-91e9-8bb2764df591)
![image](https://github.com/user-attachments/assets/c5ee5a72-9fb0-4fe1-9ad3-b677c4690296)


A Command Line Interface (CLI) Task Manager written in Python. This tool allows users to manage tasks, track their statuses, and create/manage multiple task lists. It is simple, easy to use, and operates through a terminal or command prompt.

## Features
* Task Management: Add, remove, list, and update tasks.
* Task Status: Tasks can be marked with the following statuses:
  - "Rozpoczęte" (In Progress)
  - "Wstrzymane" (Paused)
  - "Zakończone" (Completed)
* Multiple Task Lists: Support for multiple task lists, allowing you to switch between different sets of tasks.
* File Persistence: Task lists are saved in JSON format, ensuring that your tasks persist across sessions.
* Help System: Built-in help command that lists available commands.

## Prerequisites
* Python 3.x or higher

## Usage
You can run the Task Manager in interactive mode or pass commands as arguments when starting the program.
### Interactive Mode
Simply run the script:
  ```sh
python TaskManager.py
  ```
This will launch an interactive prompt where you can type commands.

### Command Line Arguments
You can also pass commands directly when starting the program. Example:
 ```sh
python TaskManager.py add " List_name; task_name; Task description"
  ```

## Comands 

### Add Task:
 ```sh
python TaskManager add <name_list>; <name>; <description> 
  ```
or
 ```sh
python TaskManager add <name>; <description> 
  ```
Example:
 ```sh
python TaskManager.py add " List_name; task_name; Task description"
  ```
### List Task:
 ```sh
python TaskManager list <name_list> 
  ```
or
 ```sh
python TaskManager list 
  ```
Example:
 ```sh
python TaskManager.py list Example_List
  ```


### List All Task:

 ```sh
python TaskManager list_all <name_list> 
  ```
or
 ```sh
python TaskManager list_all
  ```
Example:
 ```sh
python TaskManager.py list_all Example_List
```
### Update Status Task

 ```sh
python TaskManager update_status <name_list> <id> <status>
  ```
or
 ```sh
python TaskManager update_status <id> <status>
  ```
Example:
 ```sh
python TaskManager.py update_status Example_List 1 2
  ```


### Remove Task
 ```sh
python TaskManager remove <name_list> <id> 
  ```
or
 ```sh
python TaskManager remove <id> 
  ```
Example:
 ```sh
python TaskManager.py remove Example_List 1 
  ```


### New List

 ```sh
python TaskManager new_list <name>
  ```
Example:
 ```sh
python TaskManager.py new_list Example_List
  ```


### Switch List

 ```sh
python TaskManager switch <name>
  ```
Example:
 ```sh
python TaskManager.py switch Example_List
  ```
This command works only in the list-switching mode. To run the script without switching the list, simply execute it without any additional parameters !!!


### List Available Lists

 ```sh
python TaskManager switch list
  ```


### Delete List

 ```sh
python TaskManager delete_list <name>
  ```
Example:
 ```sh
python TaskManager.py delete_list Example_List
  ```


## Data Storage
All task lists are stored in separate JSON files, ensuring persistent storage for each list between program runs.


## Notes
* By default, completed tasks are hidden after 7 days. You can view hidden tasks again using the list_all command.
* If a JSON file for a task list doesn't exist, it will be automatically created.
  
## Requirements
The project uses the following Python libraries:

* termcolor for colored terminal output
   ```sh
    pip install termcolor
   ```
* platform for handling platform-specific commands
* datetime for handling task dates and times
* json for reading and writing task data to/from files
* os for interacting with the operating system (e.g., for clearing the screen and managing files)
