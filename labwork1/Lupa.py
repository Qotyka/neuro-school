from Worker import Worker
from LupaFunction import LupaFunction

class Lupa(Worker):
    def __init__(self) -> None:
        # Подставляем конкретную реализацию интерфейса WorkerFunction
        super().__init__(LupaFunction())
    
    def __repr__(self) -> str:
        return "Lupa"