from pokemon import *
from normal import *
from fire import * 
from water import * 
from grass import * 
from earth import *
from electric import *
from fight import *


class Selection(Fight):
    def choose(self):
        print("choose between 1 and 6")
        A = input()
        if A == 1:
            normal_1.stats()
            print("\n","Y / N ?")
            X = input()
            if X == "Y" :
                combat = Fight(normal_1)
                combat.ready_to_fight()
            else:
                self.choose()

        elif A == 2:
            fire_2.stats()
            print("\n","Y / N ?")
            X = input()
            if X == "Y" :
                fire_2.ready_to_fight()
            else:
                self.choose()

        elif A == 3:
            water_3.stats()
            print("\n","Y / N ?")
            X = input()
            if X == "Y" :
                water_3.fight()
            else:
                self.choose()

        elif A == 4:
            earth_4.stats()
            print("\n","Y / N ?")
            X = input()
            if X == "Y" :
                earth_4.ready_to_fight()
            else:
                self.choose()            

        elif A == 5:
            electric_5.stats()
            print("\n","Y / N ?")
            X = input()
            if X == "Y" :
                electric_5.ready_to_fight()
            else:
                self.choose()

        elif A == 6:
            grass_6.stats()
            print("\n","Y / N ?")
            X = input()
            if X == "Y" :
                grass_6.ready_to_fight()
            else:
                self.choose()


select = Selection()