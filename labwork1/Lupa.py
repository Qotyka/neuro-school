from Worker import Worker
from Lupa_function import Lupa_function
class Lupa(Worker):
    def __init__(self) -> None:
        super().__init__(Lupa_function())