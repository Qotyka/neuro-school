from Worker_function import Worker_function
class Pupa_function(Worker_function):
    """
    Реализация интерфейса стратегии для класса Pupa
    """
    def run(self, lst1: list, lst2: list) -> list:
        return list(map(lambda x: x[0] - x[-1], zip(lst1, lst2)))