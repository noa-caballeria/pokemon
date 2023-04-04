from pokemon import *


class Electric(Pokemon):
    def __init__(self, LP=500, ATK=200, DEF=10, name="Zappizor"):
        Pokemon.__init__(self, LP, ATK, DEF)
        self.name = name

    def stats(self):
        print(self.name,"\n","\n","LP = ", self.LP,"\n","ATK = ", self.ATK,"\n","DEF = ", self.DEF)

electric_5 = Electric()