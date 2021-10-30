from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for task in self.tasks:
            if new_task.name == task.name:
                return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        tasks_count = 0
        for x in self.tasks:
            if x.completed:
                tasks_count += 1
                self.tasks.remove(x)
        return f"Cleared {tasks_count} tasks."

    def view_section(self):
        result = f'Section {self.name}:'

        for task in self.tasks:
            result += '\n'
            result += task.details()

        return result