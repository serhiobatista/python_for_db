class Stack:
    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        info = ""
        for el in sorted(self.task.keys()):
            info += str(el) + " " + str(self.task[el]) + ";\n"
        return info

    def new_task(self, task, priority):
        if not priority in self.task.keys():
            self.task[priority] = Stack()
            self.task[priority].push(task)
        else:
            new_stack = Stack()
            value = self.task[priority].pop()
            if value != task:
                new_stack.push(value)
            new_stack.push(task)
            self.task[priority] = new_stack

    def pop_task(self, priority):
        self.task.pop(priority)
