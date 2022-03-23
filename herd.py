from dino import Dino

class Herd:
    def __init__(self,):
        self.dino_list = []
        pass

    def create_herd(self):
        dino_one = Dino('T-Rex')
        dino_two = Dino('Raptor')
        dino_three = Dino('Aligator')
        self.dino_list.append(dino_one)
        self.dino_list.append(dino_two)
        self.dino_list.append(dino_three)
        pass