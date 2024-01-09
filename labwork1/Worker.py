from WorkerFunction import WorkerFunction

class Worker:
    def __init__(self, function_: WorkerFunction) -> None:
        """
        Родительский класс для Pupa и Lupa
        Поле _function - функция (реализация стратегии), которую выполняют дочерние классы при вызове do_work
        Поле _completed_tasks - счетчик выполненных тасков, за которые будет начисляться ЗП
        Поле _money - счетчик денег
        """
        self._money = 0
        self._completed_tasks = 0
        self._function = function_

    def take_salary(self, money_amount):
        self._money += money_amount
    
    def do_work(self, lst1: list, lst2: list):
        print(self.__repr__(), "completed the task: ", *self._function.run(lst1, lst2))
        # Пополняем счетчик выполненных тасков
        self._completed_tasks += 1
    
    def clear_completed_tasks(self):
        """
        Сбрасывает счетчик выполненных тасков
        Данный метод вызывется в Accountant после выдачи ЗП
        """
        self._completed_tasks = 0

    @property
    def completed_tasks(self):
        return self._completed_tasks
    
    @property
    def money(self):
        return self._money