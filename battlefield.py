from herd import Herd
from fleet import Fleet


class Battlefield:
    def __init__(self):
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
                input('Dino Team will go first!!')
                return self.dino_turn()

            elif int(first_team) == 2:
                input('Robot Team will go first!!')
                return self.robo_turn()
            else:
                print('select a different number!')
                return
               
    def dino_turn(self, dino):
        # dino_fleet = Herd()
        # for dino in dino_fleet.name:
        #     print(dino)
        print(f'Your current team status ! ')
        print(input('Which robot would you like to attack?: '))
        if self.battle == 1:
            for dino in Fleet.dino:
                print(dino.name)
            self.dino.attack(self.robot)
           
            print(f'{self.dino.name} attacked {self.robot.name} for {self.attack_power}! ')
            


    def robo_turn(self):
        if self.battle == 2:
            self.dino.attack(self.robot)
            print(f'{self.dino.name} attacked {self.robot.name} for {self.attack_power}! ')
            


    def show_dino_opponent_options(self):
        # print(f'{self.Herd()}')
        print('KEEP FIGHTING THE ROBOTS!!!')
        pass


    def show_robo_opponent_options(self):
        pass


    
    def display_winners(self):
        pass