class User:
    def __init__(self, name, uid, mail):
        self.name = name
        self.uid = uid
        self.mail = mail


class Developer(User):
    def __init__(self, name, uid, mail):
        super().__init__(name, uid, mail)
        self.role = "DEVELOPER"
        self.tasks = []

    def start_task(self, task):
        if task not in self.tasks:
            print(f"{task.title} doesnot belong to the {self.name} developer")
            return

        task.start_task()

    def complete_task(self, task):
        if task not in self.tasks:
            print(f"{task.title} doesnot belong to the {self.name} developer")
            return

        task.complete_task()

    def show_tasks(self):
        res = ""

        if len(self.tasks) == 0:
            print(f"no tasks assigned to {self.name}")
            return
        else:
            res += f"\nTask assigned to {self.name}"
            res += "\nid\ttitle\tpriority\tstatus\tassigned user\tdescription"

        for task in self.tasks:
            res += f"\n{task.tid}\t{task.title}\t{task.priority}\t{task.status}\t{task.assigned_user}\t{task.desc}"

        print(res)


class Manager(User):
    def __init__(self, name, uid, mail):
        super().__init__(name, uid, mail)
        self.role = "MANAGER"

    def assign_task(self, task, dev):
        if not task:
            print("invalid task provided")
            return
        if not dev:
            print("invalid developer provided")
            return
        task.assign_task(dev)


class Task:
    def __init__(self, tid, title, desc, priority, status):
        if not tid or not title or not desc:
            raise ValueError("Values should not be empty")

        if priority not in ["LOW", "MEDIUM", "HIGH"]:
            raise ValueError("Invalid priority")

        if status not in ["TODO", "IN_PROGRESS", "DONE"]:
            raise ValueError("Invalid status")

        self.tid = tid
        self.title = title
        self.desc = desc
        self.priority = priority
        self._status = status
        self.assigned_user = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ["TODO", "IN_PROGRESS", "DONE"]:
            raise ValueError("Invalid status")

        self._status = value

    def assign_task(self, dev):
        if self in dev.tasks:
            print(f"task {self.title} is already assigned to {dev.name}")
        else:
            dev.tasks.append(self)
            self.assigned_user = dev

    def start_task(self):
        if self.status == "DONE":
            print(f"{self.title} is already completed")
        elif self.status == "IN_PROGRESS":
            print(f"{self.title} is already started")
        elif self.status == "TODO":
            print(f"{self.title} started!")
            self.status = "IN_PROGRESS"

    def complete_task(self):
        if self.status == "DONE":
            print(f"{self.title} is already completed")
        elif self.status == "TODO":
            print(f"{self.title} hasn't started Yet")
        elif self.status == "IN_PROGRESS":
            print(f"{self.title} is marked as Completed")
            self.status = "DONE"


class Project:
    def __init__(self, name, pid, mgr):
        self.name = name
        self.pid = pid
        self.manager = mgr
        self.tasks = []

    def add_task(self, task):
        if not task:
            print("task is invalid to enter")
            return

        self.tasks.append(task)

    def remove_task(self, task):
        if task not in self.tasks:
            print(f"{task.title} task is not in {self.name} project")
            return

        self.tasks.remove(task)

    def show_tasks(self):
        res = ""

        if len(self.tasks) == 0:
            print("no tasks available in this project")
            return
        else:
            res += f"\nTask in {self.name}"
            res += "\nid\ttitle\tpriority\tstatus\tassigned user\tdescription"

        for task in self.tasks:
            res += f"\n{task.tid}\t{task.title}\t{task.priority}\t{task.status}\t{task.assigned_user.name}\t{task.desc}"

        print(res)

    def find_task(self, task):
        if task in self.tasks:
            return task
        print(f"task is not present in {self.name} project")

    def __str__(self):
        res = ""

        if len(self.tasks) == 0:
            return "no tasks available in this project"
        else:
            res += f"Project: {self.name}"
            res += f"\nTotal Tasks: {len(self.tasks)}"
            res += f"\nCompleted: {len([task for task in self.tasks if task.status == 'DONE'])}"
            res += f"\nIn Progress: {len([task for task in self.tasks if task.status == 'IN_PROGRESS'])}"
            res += (
                f"\nTodo: {len([task for task in self.tasks if task.status == 'TODO'])}"
            )
        return res


# -------------------------
# TESTING
# -------------------------

# Create users
manager = Manager("Alice", 101, "alice@company.com")
developer1 = Developer("John", 102, "john@company.com")
developer2 = Developer("Sarah", 103, "sarah@company.com")


# Create project
project = Project("E-Commerce Platform", 1, manager)


# Create tasks
task1 = Task(
    1,
    "Build Login API",
    "Create login and authentication API",
    "HIGH",
    "TODO",
)

task2 = Task(
    2,
    "Fix Logout Bug",
    "Fix logout issue in the application",
    "MEDIUM",
    "TODO",
)

task3 = Task(
    3,
    "Payment Integration",
    "Integrate payment gateway",
    "HIGH",
    "TODO",
)


# Add tasks to project
project.add_task(task1)
project.add_task(task2)
project.add_task(task3)


# Manager assigns tasks
manager.assign_task(task1, developer1)
manager.assign_task(task2, developer1)
manager.assign_task(task3, developer2)


# Show project tasks
project.show_tasks()


# Show developer tasks
developer1.show_tasks()
developer2.show_tasks()


# Developer starts a task
print("\n--- Starting Task ---")
developer1.start_task(task1)

print(f"Task status: {task1.status}")


# Developer completes the task
print("\n--- Completing Task ---")
developer1.complete_task(task1)

print(f"Task status: {task1.status}")


# Show project summary
print("\n--- Project Summary ---")
print(project)


# Try invalid operation
print("\n--- Invalid Operation ---")
developer2.complete_task(task1)
