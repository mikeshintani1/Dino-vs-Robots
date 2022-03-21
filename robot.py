from weapon import Weapon



class Robot:
    def __init__(self, name, int):
        self.name = name
        self.health = int
        self.weapon = Weapon('Ray-gun')
        

    def activate_weapon(self):
        self.weapon.activated = not self.weapon.activated
        if self.weapon.activated:
            print('Ray-gun is READY!')
        else:
            print('Ray-gun is NOT READY!! ')

    def attack(self, dino):
        self.weapon_charged()
        if self.weapon_charged:
            self.weapon_charged = self.dino_health - 3
            print(f'{self.name} blasts {dino.name} with ray-gun!! ')
        elif self.weapon_charged:
            self.weapon_charged = dino.health <= 0
            print(f'{dino.name} has been killed!! ON TO THE NEXT!!')
        else:
            print('Need to turn the weapon on!! ')

