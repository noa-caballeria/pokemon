from pokemon import *


class Normal(Pokemon):
    def __init__(self, LP=200, ATK=100, DEF=110, name="Pegatinum"):
        Pokemon.__init__(self, LP, ATK, DEF)
        self.name = name

    def normal_stats(self):
        print(self.name,"\n","\n","LP = ", self.LP,"\n","ATK = ", self.ATK,"\n","DEF = ", self.DEF)

normal_1 = Normal()