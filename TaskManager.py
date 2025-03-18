import os
import json
import platform
from datetime import datetime
from termcolor import colored
from Task import Task

class TaskManager:

    STATUS_OPTIONS = {"1": "Rozpoczęte", "2": "Wstrzymane", "3": "Zakończone"}
    HIDE_AFTER_DAYS = 7 


    
    def __init__(self):
        self.current_list = "default.json"
        self.tasks = self.load_tasks()

    # Wczytuje listę zadań z pliku
    def load_tasks(self):
        if os.path.exists(self.current_list):
            with open(self.current_list, "r") as file:
                return [Task.from_dict(task) for task in json.load(file)]
        return []

    # Zapisuje listę zadań do pliku
    def save_tasks(self):
        with open(self.current_list, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    # Dodaje nowe zadanie
    def add_task(self, name, description):
        if not name or not description:
            print(colored("Nazwa i opis zadania są wymagane!", 'orange'))
            return
        self.tasks.append(Task(name, description))
        self.save_tasks()
        print(colored("Zadanie dodane.", 'green'))


    # Wyświetla listę zadań
    def list_tasks(self, status_filter=None):
        if not self.tasks:
            print(colored("Brak dostępnych zadań.", 'red'))
            return

        today = datetime.today()
        recent_tasks = []

        for index, task in enumerate(self.tasks, start= 1): 
            
            # Filtrujemy zadania młodsze niż 7 dni
            if task.created_at is None or (today - task.created_at).days <= self.HIDE_AFTER_DAYS:
                recent_tasks.append((index, task))

        print(colored(f"Pełna lista zadań ({self.current_list}):\n", 'cyan'))

        if recent_tasks:
            print(colored("🟢 Aktywne zadania:", 'green'))
            for i, (index,task) in enumerate(recent_tasks, 1):
                task_str = colored(f"{i}. < ID: {index} > - {task.name} - {task.description} - Status: ({task.status})", self.get_status_color(task.status))
                print(task_str)
        else:
            print(colored("Brak aktywnych zadań.", 'yellow'))


    # Wyświetla pełną listę zadań
    def list_tasks_all(self, status_filter=None):
        if not self.tasks:
            print(colored("Brak dostępnych zadań.", 'red'))
            return
        
        today = datetime.today()
        recent_tasks = []
        old_tasks = []

        for index, task in enumerate(self.tasks, start= 1):  
            if task.created_at is None or (today - task.created_at).days < self.HIDE_AFTER_DAYS:
                recent_tasks.append((index, task))  
            else:
                old_tasks.append((index, task))  

        print(colored(f"Pełna lista zadań ({self.current_list}):\n", 'cyan'))

        if recent_tasks:
            print(colored("🟢 Aktywne zadania:", 'green'))
            for i, (index, task) in enumerate(recent_tasks, 1):
                task_str = colored(f"{i}. < ID: {index} > - {task.name} - {task.description} - Status: ({task.status})", self.get_status_color(task.status))
                print(task_str)
        else:
            print(colored("Brak aktywnych zadań.", 'yellow'))

        if old_tasks:
            print("\n" + colored(f"🔴 Zadania starsze niż {self.HIDE_AFTER_DAYS} dni:", 'red'))
            for i, (index, task) in enumerate(old_tasks, 1):
                task_str = colored(f"{i}. < ID: {index} > - {task.name} - {task.description} - Status: ({task.status})", self.get_status_color(task.status))
                print(task_str)
        else:
            print("\n" + colored("Brak starszych zadań.", 'yellow'))

    # Zwraca kolor statusu zadania
    def get_status_color(self, status):
      
        return {
            "Rozpoczęte": "yellow",
            "Wstrzymane": "red",
            "Zakończone": "green"
        }.get(status, "white")


    # Aktualizuje status zadania
    def update_task(self, task_id, status):
        try:
            task = self.tasks[task_id - 1]  
            if status in self.STATUS_OPTIONS:
                task.status = self.STATUS_OPTIONS[status]
                self.save_tasks()
                print(colored(f"Status zadania '{task.name}' zaktualizowany na: {task.status}" , 'yellow'))
            else:
                print(colored("Nieprawidłowy status!", 'red'))
        except IndexError:
            print(colored("Nie znaleziono zadania o podanym ID!",'red'))


    # Usuwa zadanie
    def remove_task(self, task_id):
        if not self.tasks:
            print(colored("Brak dostępnych zadań do usunięcia.", "red"))
            return
        
        try:
            task_id = int(task_id) - 1
            if 0 <= task_id < len(self.tasks):
                deleted_task = self.tasks.pop(task_id)
                self.save_tasks()
                print(colored(f"Zadanie '{deleted_task.name}' zostało usunięte.", "green"))
            else:
                print(colored("Nieprawidłowy numer zadania.", "red"))
        except ValueError:
            print(colored("ID zadania musi być liczbą!", "red"))

    #===============================================================================================================


    # Usuwa listę zadań
    def delete_list(self, name):
        """ Usuwa listę zadań """
        filename = f"{name}.json"
        if os.path.exists(filename):
            os.remove(filename)
            print(colored(f"Lista '{name}' została usunięta.", "green"))
            if self.current_list == filename:
                self.current_list = "default.json"
                self.tasks = self.load_tasks()
                print(colored("Przełączono na domyślną listę zadań.", "yellow"))
        else:
            print(colored(f"Lista '{name}' nie istnieje.", "red"))
        
    # Przełącza na inną listę zadań    
    def switch_task_list(self, name):
        filename = f"{name}.json"
        
        if os.path.exists(filename):
            self.current_list = filename
            self.tasks = self.load_tasks()
            print(colored(f"Przełączono na listę: {name}", 'green'))
        else:
            print(colored(f"Lista '{name}' nie istnieje. Użyj 'new_list {name}', aby ją utworzyć.", 'red'))


    # Tworzy nową listę zadań
    def create_new_list(self, name):
        self.current_list = f"{name}.json"
        self.tasks = []
        self.save_tasks()
        print(colored(f"Utworzono nową listę: {name}", 'green'))


    # Wyświetla dostępne listy zadań
    def display_lists(self):
        files = [f[:-5] for f in os.listdir() if f.endswith(".json")]
        print(colored("Dostępne listy zadań:", 'cyan'))
        for file in files:
            print(f"- {file}")

# ===============================================================================================================
    # Czyści ekran konsoli
    def clear_screen(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")


    # Obsługa komend
    def handle_command(self, command):
        self.clear_screen()
        parts = command.split(" ", 1)
        cmd = parts[0]
        args = parts[1] if len(parts) > 1 else ""

        match cmd:
            case "add":
                name_desc = args.split(";", 1)
                if len(name_desc) < 2:
                    print("Użycie: add <nazwa>; <opis>")
                    return
                self.add_task(name_desc[0].strip(), name_desc[1].strip())
            case "list":
                self.list_tasks()
            case "list_all":
                self.list_tasks_all()
            case "update_status":
                args_split = args.split(" ", 1)
                if len(args_split) < 2:
                    print("Użycie: update_status <id> <status>")
                    print("Dostępne statusy: 1 - Rozpoczęte, 2 - Wstrzymane, 3 - Zakończone")
                    return
                task_id, status = args_split[0], args_split[1]
                self.update_task(int(task_id), status)
            case "switch":
                self.switch_task_list(args)
            case "remove":
                self.remove_task(args)
            case "new_list":
                self.create_new_list(args)
            case "lists":
                self.display_lists()
            case "delete_list":
                self.delete_list(args)
            case "help":
                self.show_help()
            case "exit":
                exit()
            case _:
                print("Nieznana komenda. Wpisz 'help', aby zobaczyć dostępne komendy.")

    # Pomoc 
    def show_help(self):
        print("Dostępne komendy:")

         # Sekcja zadań
        print(colored("Zadania:", 'cyan'))
        print(colored("   > add <nazwa>; <opis>       - Dodaje nowe zadanie", 'green'))
        print("   > list                      - Wyświetla listę aktywnych zadań")
        print("   > list_all                  - Wyświetla pełną listę zadań (również te zakończone)")
        print("   > update_status <id> <status>      - Aktualizuje status zadania")
        print(colored("   > remove <id>               - Usuwa zadanie", 'red'))

        # Sekcja list
        print(colored("Listy:", 'cyan'))
        print(colored("   > new_list <nazwa>          - Tworzy nową listę zadań", 'green'))
        print("   > switch <nazwa>            - Przełącza na inną listę zadań")
        print("   > lists                     - Wyświetla dostępne listy")
        print(colored("   > delete_list <nazwa>       - Usuwa listę zadań", 'red'))
        
        # Pozostałe komendy
        print(colored("Pozostałe:", 'cyan'))
        print("   > help                      - Wyświetla pomoc")
        print("   > exit                      - Zamyka program")


def main():
    manager = TaskManager()
    print("Task Manager CLI. Wpisz 'help', aby zobaczyć dostępne komendy.")
    while True:
        command = input("\nKomenda: ")
        manager.handle_command(command)

if __name__ == "__main__":
    main()
