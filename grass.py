from pokemon import *


class Grass(Pokemon):
    def __init__(self, LP=230, ATK=90, DEF=90, name="Spikan"):
        Pokemon.__init__(self, LP, ATK, DEF)
        self.name = name

    def stats(self):
        print(self.name,"\n","\n","LP = ", self.LP,"\n","ATK = ", self.ATK,"\n","DEF = ", self.DEF)

grass_6 = Grass()