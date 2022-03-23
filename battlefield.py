

from unicodedata import name
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
            # print(f"The dino herd has assembled! {Herd.dino.dino_one.name} ({Herd.dino.dino_one.health} HP), {Herd.dino.dino_two.name} ({Herd.dino.dino_two.health} HP), and {Herd.dino.dino_three.name} ({Herd.dino.dino_three.health} HP.)")
            select_target = input("Enter choice to attack! <1> for 'Nokia' <2> for 'Samsung' <3> for 'Asus' ")
            for dino in self.herd.dinos:
                print(dino.name)
            if select_target == "1":
                print(f"{self.herd.dinos[1]} has been attacked! ")
            elif select_target == "2":
                print(f"{self.herd.dinos} has been attacked! ")
            elif select_target == "3":
                print(f"{self.herd.dinos} has been attacked! ")
            pass


    def robo_turn(self):
        for robot in self.fleet.robot:
                print(robot.list)

                # attack = input("Press Y to launch attack!:  ")
                # herd = Herd.create_herd

                # select_target = input("Enter choice to attack! <1> for 'T-Rex' <2> for 'Raptor' <3> for 'Aligator' ")
                # if select_target == "1":
                #  herd = Herd.create_herd[0]
                # elif select_target == "2":
                #     herd = Herd.create_herd[1]
                # elif select_target == "3":
                #     herd = Herd.create_herd[2]
                pass


    def show_robo_opponent_options(self):
        # for dino in self.herd.dino_list:
        #         print(dino.name)
        pass


    
    def display_winners(self):
        pass