

from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self,):
        self.fleet = Fleet()
        self.herd = Herd()
        

    def run_game(self):
        self.run_game = input('Press 1 to start game!: ')
        self.display_welcome()
        self.battle()
        self.dino_turn()
        self.robo_turn()
        self.display_winners()


    def display_welcome(self):
        if self.run_game == str(1):
            print('+++++++ WELCOME TO ROBOTS VERSUS DINOSAURS +++++++++')
        else:
            return    


    def battle(self):
            first_team = input('Choose which team will go first! 1 for Dinos! 2 for Robots! ')
            if int(first_team) == 1:
                print('Dino Team will go first!!')
                

            elif int(first_team) == 2:
                print('Robot Team will go first!!')
        
               
    def dino_turn(self):
            attack = input("Press Y to launch attack!:  ")
            fleet = Fleet.create_fleet

            select_target = input("Enter choice to attack! <1> for 'Nokia' <2> for 'Samsung' <3> for 'Asus' ")
            if select_target == "1":
                fleet = Fleet[0]
            elif select_target == "2":
                fleet = Fleet.create_fleet[1]
            elif select_target == "3":
                fleet = Fleet.create_fleet[2]

            
                print(f'{self.dino.name} attacked {self.robot.name} for {self.attack_power}! ')
            


    def robo_turn(self):
            attack = input("Press Y to launch attack!:  ")
            herd = Herd.create_herd

            select_target = input("Enter choice to attack! <1> for 'T-Rex' <2> for 'Raptor' <3> for 'Aligator' ")
            if select_target == "1":
                herd = Herd.create_herd[0]
                return self.battle
            elif select_target == "2":
                herd = Herd.create_herd[1]
            elif select_target == "3":
                herd = Herd.create_herd[2]


    def show_robo_opponent_options(self):
        pass


    
    def display_winners(self):
        pass