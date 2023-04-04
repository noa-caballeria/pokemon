from pokemon import *


class Fire(Pokemon):
    def __init__(self, LP=330, ATK=130, DEF=60, name="Komainu"):
        Pokemon.__init__(self, LP, ATK, DEF)
        self.name = name

    def stats(self):
        print(self.name,"\n","\n","LP = ", self.LP,"\n","ATK = ", self.ATK,"\n","DEF = ", self.DEF)

fire_2 = Fire()