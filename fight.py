from selection import *
from fire import *
from water import *
from grass import *
from earth import *
from electric import *
from normal import *
import random


class Fight():    
    def __init__(self, mon_pokemon):
        self.mon_pokemon = mon_pokemon
        pokemon_list = [normal_1, fire_2, water_3, earth_4, electric_5, grass_6]
        self.opp_pokemon = random.choice(pokemon_list)
        print("Your Opponent's Pokemon is :", self.opp_pokemon)

    def ready_to_fight(self):
        self.mon_pokemon.stats()
        self.opp_pokemon.stats()
        



combat = Fight()
combat.fighting()