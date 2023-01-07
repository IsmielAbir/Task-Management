import datetime
import uuid

class TaskManagement:
    def __init__(self,task, id=None, createdTime=None, updatedTime=None, completed=False, completedTime=None) -> None:
        self.task = task
        self.id = id or uuid.uuid4()
        self.createdTime = createdTime or datetime.datetime.now()
        self.updatedTime = updatedTime or createdTime
        self.completed = completed
        self.completedTime = completedTime
        
    def updateTask(self, newTask):
        self.task = newTask
        self.updatedTime = datetime.datetime.now()
        
    def completeTask(self):
        self.completed = True
        self.completedTime = datetime.datetime.now()
        

class Task():
    def __init__(self, createdTime=None, updatedTime=None, completed=False, completedTime=None) -> None:
        self.tasks = []
        self.createdTime = createdTime or datetime.datetime.now()
        self.updatedTime = updatedTime or createdTime
        self.completed = completed
        self.completedTime = completedTime
        
    def add_task(self, taskName):
        t = TaskManagement(taskName)
        self.tasks.append(t)
        print(f"\nTask '{t.task}' created sucessfully")
    def all_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"\nId: {uuid.uuid4()}\nTask Id: {i+1}\nTask Name: {task.task}\nCreated Time: {self.createdTime}\nUpdated Time: {self.updatedTime}\nCompleted Task: {self.completed}\nCompleted Time: {self.completedTime}")
            
    def incomplete_tasks(self):
        for i, task in enumerate(self.tasks):
            if not task.completed:
                print(f"\nId: {uuid.uuid4()}\nTask Id: {i+1}\nTask Name: {task.task}\nCreated Time: {self.createdTime}\nUpdated Time: {self.updatedTime}\nCompleted Task: {self.completed}\nCompleted Time: {self.completedTime}")
    def complete_tasks(self):
        for i, task in enumerate(self.tasks):
            if task.completed:
                print(f"\nId: {uuid.uuid4()}\nTask Id: {i+1}\nTask Name: {task.task}\nCreated Time: {self.createdTime}\nUpdated Time: {self.updatedTime}\nCompleted Task: {self.completed}\nCompleted Time: {self.completedTime}")
     
    def update_task(self, task_index, new_task_name):
        try:
            for i, task in enumerate(self.tasks):
                task = self.tasks[task_index-1]
                task.updateTask(new_task_name)
            print(f"Task '{task.task}' updated successfully")
        except IndexError:
            print(f"Invalid task index: {task_index}")
       
    def task_complete(self, task_index):
        try:
            for i, task in enumerate(self.tasks):

                task = self.tasks[task_index-1]
                task.completeTask()
            print(f"Task '{task.task}' marked as completed")
        except IndexError:
            print(f"Invalid task index: {task_index}")
               
        
        
        
        
def main():
    taskfind = Task()
    while True:
        print("\nMenu:")
        print("1. Add new task")
        print("2. Show all tasks")
        print("3. Show incomplete tasks")
        print("4. Show complete tasks")
        print("5. Update task")
        print("6. Mark task as completed")
        print("0. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            print("\n\nAdd A New Task-------------")
            task_name = input("\nEnter the task name: ")
            taskfind.add_task(task_name)
        elif choice == "2":
            print("\n\nShow All Task--------------")

            taskfind.all_tasks()
        elif choice == "3":
            print("\n\nShow Incomplete Task-------")
            taskfind.incomplete_tasks()
        elif choice == "4":
            print("\n\nShow Complete Task---------")
            taskfind.complete_tasks()
        elif choice == "5":
            task_index = int(input("Enter the task index: "))
            new_task_name = input("Enter the new task name: ")
            taskfind.update_task(task_index, new_task_name)
        elif choice == "6":
            print("\n\nMark A Task Complete-------")
            task_index = int(input("\nEnter the task index: "))
            taskfind.task_complete(task_index)
        elif choice == "0":
            break
        else:
            print("\nInvalid choice")
            
if __name__ == "__main__":
    main()

        