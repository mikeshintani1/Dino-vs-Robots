from robot import Robot

class Dino:
    def __init__(self, name):
        self.name = name
        self.attack_power = 3
        self.health = 10
        self.dino_ready = False
        

    def dino_name(self):
        self.name = ['T-Rex', 'Raptor', 'Aligator']
        print(input('Select a Dino!: '))
        

    def activate_weapon(self):
        self.dino_ready = not self.dino_ready
        if self.dino_ready:
            print('DINO READY TO ATTACK!')
        else:
            print('Dino need nappy nap')
            pass

    def attack(self, robot):
        if self.dino_charged:
            self.dino_charged = self.robot_health - 3
            print(f'{self.name} bites off a big chunk of {robot.name}!! ')
        elif self.weapon_charged:
            self.dino_charged = robot.health <= 0
            print(f'{robot.name} has been killed!! ON TO THE NEXT!!')
        else:
            print('Dino looking at butterflies!! ')
            pass
