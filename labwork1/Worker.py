from Worker_function import Worker_function

class Worker:
    def __init__(self, function_: Worker_function) -> None:
        self._money = 0
        self._completed_tasks = 0
        self._function = function_

    def take_salary(self, money_):
        self._money += money_
    
    def do_work(self, lst1: list, lst2: list):
        print(self._function.run(lst1, lst2))
        self._completed_tasks += 1
    
    def clear_completed_tasks(self):
        self._completed_tasks = 0

    @property
    def completed_tasks(self):
        return self._completed_tasks
    
    @property
    def money(self):
        return self._money