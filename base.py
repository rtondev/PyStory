from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict

class Fase(ABC):
    @abstractmethod
    def executar(self):
        pass

@dataclass
class Item:
    nome: str
    descricao: str
    emoji: str
    quantidade: int = 1

@dataclass
class Status:
    saude: int = 100
    hidratacao: int = 100
    energia: int = 100
    sanidade: int = 100
    conhecimento: int = 0

class Inventario:
    def __init__(self):
        self.items: Dict[str, Item] = {}
        
    def adicionar_item(self, item: Item):
        if item.nome in self.items:
            self.items[item.nome].quantidade += item.quantidade
        else:
            self.items[item.nome] = item
            
    def remover_item(self, nome_item: str, quantidade: int = 1):
        if nome_item in self.items:
            self.items[nome_item].quantidade -= quantidade
            if self.items[nome_item].quantidade <= 0:
                del self.items[nome_item]
                
    def tem_item(self, nome_item: str) -> bool:
        return nome_item in self.items

class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.inventario = Inventario()
        self.status = Status()
        self.conquistas: List[str] = []
        
    def adicionar_conquista(self, conquista: str):
        if conquista not in self.conquistas:
            self.conquistas.append(conquista)
            
    def atualizar_status(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self.status, key):
                current = getattr(self.status, key)
                setattr(self.status, key, max(0, min(100, current + value)))