

class Dino:
    def __init__(self, name):
        self.name = name
        self.attack_power = 3
        self.health = 10
        

    def dino_name(self):
        self.name = ['T-Rex', 'Raptor', 'Aligator']
        print(input('Select a Dino!: '))
        

    def activate_weapon(self):
        self.dino.ready = not self.dino.ready
        if self.dino.ready:
            print('DINO READY TO ATTACK!')
        else:
            print('Dino need nappy nap')
            pass

    def attack(self, robot):
        self.dino_charged()
        if self.dino_charged:
            self.dino_charged = self.robot_health - 3
            print(f'{self.name} bites off a big chunk of {robot.name}!! ')
        elif self.weapon_charged:
            self.dino_charged = robot.health <= 0
            print(f'{robot.name} has been killed!! ON TO THE NEXT!!')
        else:
            print('Dino looking at butterflies!! ')
            pass

class House:
    def __init__(self, owner, square_feet) -> None:
        self.owner = owner
        self.square_feet = square_feet


class Neighborhood:
    def __init__(self) -> None:
        self.houses = [House("JJ", 400000), House("Susan", 600000)]


# birnam_wood = Neighborhood()

# # GOAL: Get the owner value for the first house in the Neighborhood

# # print(birnam_wood.houses[0].owner)

# for house in birnam_wood.houses:
#     print(house.owner)

# dino_fleet = Dino()
# for dino in dino_fleet.name:
#     print(dino)