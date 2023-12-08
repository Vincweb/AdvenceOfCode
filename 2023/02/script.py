# Advent Of Code 2023
# Day 2: Cube Conundrum
# By Vincweb

import re
import functools 

# Spécifiez le chemin du fichier que vous souhaitez lire
input_file = './input.txt'
nb_red = 12
nb_green = 13
nb_blue = 14

sum = 0
sum_power = 0

class Game:
    def __init__(self, input_text):
        self.game_id = 0
        self.game_sets = []
        self.max_red = 0
        self.max_green = 0
        self.max_blue = 0
        self.parse_input_text(input_text)

    def parse_input_text(self, input_text):
        
        parts = input_text.split(':')

        # Extraire les Game Sets
        self.game_sets = parts[1].split(';')

        # Utiliser une expression régulière pour extraire ID game
        match = re.match(r"Game (\d+)", parts[0])
        if match:
            self.game_id = int(match.group(1))
        else:
            print("Format ID Game incorrect.")

    def is_possible(self, max_red, max_green, max_blue):
        
        for set in self.game_sets:
        
          match_red = re.match(r".*?(\d+) red", set)
          if match_red:
              red = int(match_red.group(1))
              if red > max_red:
                return False
              
          match_green = re.match(r".*?(\d+) green", set)
          if match_green:
              green = int(match_green.group(1))
              if green > max_green:
                return False
          
          match_blue = re.match(r".*?(\d+) blue", set)
          if match_blue:
              blue = int(match_blue.group(1))
              if blue > max_blue:
                return False

        return True
    
    def max_color(self):
       
        for set in self.game_sets:
        
          match_red = re.match(r".*?(\d+) red", set)
          if match_red:
              red = int(match_red.group(1))
              if red > self.max_red:
                self.max_red = red
              
          match_green = re.match(r".*?(\d+) green", set)
          if match_green:
              green = int(match_green.group(1))
              if green > self.max_green:
                self.max_green = green
          
          match_blue = re.match(r".*?(\d+) blue", set)
          if match_blue:
              blue = int(match_blue.group(1))
              if blue > self.max_blue:
                self.max_blue = blue

        return [self.max_red, self.max_green, self.max_blue]
       

# Ouvrez le fichier en mode lecture
with open(input_file, 'r') as fichier:
    # Lisez chaque ligne du fichier
    for ligne in fichier:
        # Enregistrer la partie
        game_played = Game(ligne)

        # Accéder aux variables
        if game_played.is_possible(nb_red, nb_green, nb_blue):
          sum = sum + game_played.game_id

        sum_power = sum_power + functools.reduce(lambda a, b: a*b, game_played.max_color())

print(sum)
print(sum_power)