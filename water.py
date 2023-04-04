from pokemon import *


class Water(Pokemon):
    def __init__(self, LP=180, ATK=70, DEF=120, name ="Shakoblad"):
        Pokemon.__init__(self, LP, ATK, DEF)
        self.name = name

    def stats(self):
        print(self.name,"\n","\n","LP = ", self.LP,"\n","ATK = ", self.ATK,"\n","DEF = ", self.DEF)

water_3 = Water()