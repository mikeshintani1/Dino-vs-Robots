<<<<<<< HEAD
from herd import Herd
from fleet import Fleet
=======
from fleet import Fleet
from herd import Herd


>>>>>>> 9eadf9b252ffa377223cc077cc6d4477e5d4ca8f


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        

    def run_game(self):
        self.run_game = input('Press 1 to start game!: ')
<<<<<<< HEAD
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
=======
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
               


>>>>>>> 9eadf9b252ffa377223cc077cc6d4477e5d4ca8f

            elif int(first_team) == 2:
                input('Robot Team will go first!!')
                return self.robo_turn()
            else:
                print('select a different number!')
                return
               
    def dino_turn(self, dino):
<<<<<<< HEAD
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
            
=======
        if self.battle == 1:
            self.dino.attack(self.robot)
            print(f'{self.dino.name} attacked {self.robot.name} for {self.attack_power}! ')
>>>>>>> 9eadf9b252ffa377223cc077cc6d4477e5d4ca8f


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
       
