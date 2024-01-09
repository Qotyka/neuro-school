from Worker import Worker
from PupaFunction import PupaFunction

class Pupa(Worker):
    def __init__(self) -> None:
        # Подставляем конкретную реализацию интерфейса WorkerFunction
        super().__init__(PupaFunction())
    
    def __repr__(self) -> str:
        return "Pupa"