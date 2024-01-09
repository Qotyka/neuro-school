from Worker import Worker

class Accountant:
    def give_salary(self, worker: Worker):
        # Начисляем по 100 баксов за выполненный таск и чистим количество выполненных тасков
        worker.take_salary(worker.completed_tasks*100)
        worker.clear_completed_tasks()