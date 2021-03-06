from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if any([x for x in self.tasks if x.name == new_task.name]):
            return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):

        for task in self.tasks:
            if task.name == task_name:
                task.completed = True

                return f'Completed task {task_name}'

        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        result = 0

        for task in self.tasks:
            if task.completed:
                result += 1
                self.tasks.remove(task)

        return f'Cleared {result} tasks.'

    def view_section(self):
        output = f'Section {self.name}:'
        for task in self.tasks:
            output += '\n'
            output += task.details()

        return output

