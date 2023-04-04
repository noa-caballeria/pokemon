from pokemon import *


class Earth(Pokemon):
    def __init__(self, LP=50, ATK=60, DEF=300, name="Mayarex"):
        Pokemon.__init__(self, LP, ATK, DEF)
        self.name = name

    def stats(self):
        print(self.name,"\n","\n","LP = ", self.LP,"\n","ATK = ", self.ATK,"\n","DEF = ", self.DEF)

earth_4 = Earth()
