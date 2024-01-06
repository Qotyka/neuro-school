from Worker_function import Worker_function
class Lupa_function(Worker_function):
    """
    Реализация интерфейса стратегии для класса Lupa
    """
    def run(self, lst1: list, lst2: list) -> list:
        return list(map(sum, zip(lst1, lst2)))