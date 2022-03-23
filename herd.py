from dino import Dino

class Herd:
    def __init__(self):
        self.dinos = []
        

    def create_herd(self):
        dino_one = Dino('T-Rex')
        dino_two = Dino('Raptor')
        dino_three = Dino('Aligator')
        self.dinos.append(dino_one)
        self.dinos.append(dino_two)
        self.dinos.append(dino_three)
        