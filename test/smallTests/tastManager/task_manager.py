from lib import *
class TaskManager:
    def __init__(self):
        self.completed = []
        self.uncompleted = []
        def read(path, var):
            with open(path, "r") as f:
                var = [n.strip() for n in f.readlines()]
        read("uncompleted.txt", self.uncompleted)
        read("completed.txt", self.completed)

    def save_tasks(self):
        with open("uncompleted.txt", "w") as f:
            f.writelines([f"{n}\n" for n in self.uncompleted])
        with open("completed.txt", "w") as f:
            f.writelines([f"{n}\n" for n in self.completed])

    def show_all(self):
        print("Uncompleted.")


    def add_task(self, task: str):
        self.uncompleted.insert(0, task)

    def remove_task(self, index):
        if (index < 0 or index > len(self.uncompleted) + 1):
            return False
        else:
            self.uncompleted.remove(self.uncompleted[index])
            return True