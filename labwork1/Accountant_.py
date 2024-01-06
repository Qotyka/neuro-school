from Worker import Worker

class Accountant:
    def __init__(self) -> None:
        self.a = 1
    def give_salary(self, worker: Worker):
        worker.take_salary(worker.completed_tasks*100)
        worker.clear_completed_tasks()