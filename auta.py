from dataclasses import dataclass


@dataclass
class Auta:
    vyrobce: str
    model: str
    objem: str
    barva: str



"""
    def __init__(self, vyrobce, model, objem, barva):
        self.vyrobce = vyrobce
        self.model = model
        self.objem = objem 
        self.barva = barva

    def __str__(self) -> str:
        return self.vyrobce + "(" + self.model + ")"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Auta) and self.vyrobce == other.vyrobce and self.model == other.model and self.objem == other.objem and self.barva == other.barva
"""