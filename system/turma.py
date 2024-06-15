from abc import ABC, abstractmethod

class Turma(ABC):
    def __init__(self, nome : str) -> None:
        self.nome = nome

