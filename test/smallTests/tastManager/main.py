from task_manager import *
from asker import *
from keyboard import is_pressed, press_and_release

# Make a ui
task_manager = TaskManager()

action_Labels = [
    "to add a Task.",
    "to remove a Task.",
    "to show all the uncompleted Tasks",
    "to show all the completed Tasks",
    "to show all tasks"
]
actions = {
    "a": task_manager.add_task,
    "r": task_manager.remove_task,
    "show": task_manager.show_all
}

while True:
    IN = input("What do you want to do: ")

# mark a task as done
