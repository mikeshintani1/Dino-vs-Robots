from fleet import Fleet
from herd import Herd




class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        pass

    def run_game(self):
        self.run_game = input('Press 1 to start game!: ')
        pass



    def display_welcome(self):
        print('+++++++ WELCOME TO ROBOTS VERSUS DINOSAURS +++++++++')



    def battle(self):
        if self.run_game == 1:
            first_team = input('Choose which team will go first! 1 for Dinos! 2 for Robots! ')
            if int(first_team) == 1:
                input('Dino Team will go first!!')
            elif int(first_team) == 2:
                input('Robot Team will go first!!')
            else:
                print('select a different number!')
                return
               



    def dino_turn(self, dino):
        if self.battle == 1:
            self.dino.attack(self.robot)
            print(f'{self.dino.name} attacked {self.robot.name} for {self.attack_power}! ')



    def robo_turn(self, robot):
        pass


    def show_dino_opponent_options(self):
        pass



    def show_robo_opponent_options(self):
        pass


    
    def display_winners(self):
       
