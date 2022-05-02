from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome, peso, idade, membros):
        self.__nome = nome
        self.__peso = peso
        self.__idade = idade
        self.__membros = membros

    @property
    def nome(self):
        return print(self.__nome)

    @property
    def peso(self):
        return print(self.__peso)

    @peso.setter
    def peso(self, new_weight):
        self.__peso = new_weight

    @property
    def idade(self):
        return print(self.__idade)

    @property
    def membros(self):
        return print(self.__membros)

    @abstractmethod
    def locomover(self):
        return print(f"{self.__nome} está andando")

    @abstractmethod
    def alimentar(self):
        return print(f"{self.__nome} está comendo")
    
    @abstractmethod
    def som(self):
        return print(f"{self.__nome} está falando")

class Mamifero(Animal):
    def __init__(self, nome, peso, idade, membros):
        super().__init__(nome, peso, idade, membros)

    def locomover(self):
        return super().locomover()

    def alimentar(self):
        return super().alimentar()

    def som(self):
        return super().som()

class Reptil(Animal):
    def __init__(self, nome, peso, idade, membros):
        super().__init__(nome, peso, idade, membros)

    def locomover(self):
        return super().locomover()

    def alimentar(self):
        return super().alimentar()

    def som(self):
        return super().som()

class Ave(Animal):
    def __init__(self, nome, peso, idade, membros):
        super().__init__(nome, peso, idade, membros)

    def locomover(self):
        return super().locomover()

    def alimentar(self):
        return super().alimentar()

    def som(self):
        return super().som()

class Peixe(Animal):
    def __init__(self, nome, peso, idade, membros):
        super().__init__(nome, peso, idade, membros)

    def locomover(self):
        return super().locomover()

    def alimentar(self):
        return super().alimentar()

    def som(self):
        return super().som()