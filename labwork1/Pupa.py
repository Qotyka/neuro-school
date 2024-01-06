from Worker import Worker
from Pupa_function import Pupa_function
class Pupa(Worker):
    def __init__(self) -> None:
        super().__init__(Pupa_function())