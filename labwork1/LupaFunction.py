from WorkerFunction import WorkerFunction

class LupaFunction(WorkerFunction):
    """
    Реализация интерфейса стратегии для класса Lupa
    """
    def run(self, lst1: list, lst2: list) -> list:
        return list(map(sum, zip(lst1, lst2)))