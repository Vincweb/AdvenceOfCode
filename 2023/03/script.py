# Advent Of Code 2023
# Day 3: Gear Ratios
# By Vincweb

import functools 

# Spécifiez le chemin du fichier que vous souhaitez lire
input_file = './input.txt'
engine = []
sum = 0
buffer = ""
valid = False

def is_symbol(letter):
   return not (letter.isdigit() or letter == '.')

def is_valid(engine, i, j):
   # Haut
   if i > 0:
      # Diagonal gauche
      if j > 0:
         if is_symbol(engine[i-1][j-1]):
            return True
         
      # Haut
      if is_symbol(engine[i-1][j]):
         return True
         
      # Diagonal droite
      if j < len(engine[i]) - 1:
         if is_symbol(engine[i-1][j+1]):
            return True
         
   # Gauche
   if j > 0:
      if is_symbol(engine[i][j-1]):
         return True
      
   # Droite
   if j < len(engine[i]) - 1:
      if is_symbol(engine[i][j+1]):
         return True
      
   # Bas
   if i < len(engine) - 1:
      # Diagonal gauche
      if j > 0:
         if is_symbol(engine[i+1][j-1]):
            return True
         
      # Bas
      if is_symbol(engine[i+1][j]):
         return True
         
      # Diagonal droite
      if j < len(engine[i]) - 1:
         if is_symbol(engine[i+1][j+1]):
            return True
   
   return False

# Ouvrez le fichier en mode lecture
with open(input_file, 'r') as fichier:
    # Lisez chaque ligne du fichier
    for ligne in fichier:  
      engine.append(ligne.strip())

for i, ligne in enumerate(engine):
   # Si le nombre est en bout de ligne et valid
   if valid:
            sum = sum + int(buffer)

   # On réinitialise le buffer et la validation
   buffer = ""
   valid = False

   for j, letter in enumerate(ligne):
      # On enregistre dans le buffer quand on commence à arriver sur un nombre
      if letter.isdigit():
         buffer = buffer + letter

         if not valid:
            valid = is_valid(engine, i, j)
      else:
         # Quand on arrive à la fin d'un nombre
         if valid:
            sum = sum + int(buffer)

         # On réinitialise le buffer et la validation
         buffer = ""
         valid = False

print(sum)

sum_ratios = 0

def is_gear(letter):
   return letter == '*'

def get_number(engine, i, j):
   buffer = engine[i][j]

   # Gauche
   x = j - 1
   while x >= 0 and engine[i][x].isdigit():
      buffer = engine[i][x] + buffer
      x = x - 1
   
   # Droite
   y = j + 1
   while y <= len(engine[i]) - 1 and engine[i][y].isdigit():
      buffer = buffer + engine[i][y]
      y = y + 1

   return buffer

def ratio(engine, i, j):
   adjacent = []
   number_tl = False
   number_t = False
   number_bl = False
   number_b = False

   # Haut
   if i > 0:
      # Diagonal gauche
      if j > 0:
         if engine[i-1][j-1].isdigit():
            number_tl = True
            adjacent.append(get_number(engine, i - 1, j - 1))
         
      # Haut
      if engine[i-1][j].isdigit():
         number_t = True
         if not number_tl:
            adjacent.append(get_number(engine, i - 1, j))
         
      # Diagonal droite
      if j < len(engine[i]) - 1:
         if engine[i-1][j+1].isdigit() and not number_t:
            adjacent.append(get_number(engine, i - 1, j + 1))

   # Gauche
   if j > 0:
      if engine[i][j-1].isdigit():
         adjacent.append(get_number(engine, i, j - 1))
      
   # Droite
   if j < len(engine[i]) - 1:
      if engine[i][j+1].isdigit():
         adjacent.append(get_number(engine, i, j + 1))
      
   # Bas
   if i < len(engine) - 1:
      # Diagonal gauche
      if j > 0:
         if engine[i+1][j-1].isdigit():
            number_bl = True
            adjacent.append(get_number(engine, i + 1, j - 1))
         
      # Bas
      if engine[i+1][j].isdigit():
         number_b = True
         if not number_bl:
            adjacent.append(get_number(engine, i + 1, j))
         
      # Diagonal droite
      if j < len(engine[i]) - 1:
         if engine[i+1][j+1].isdigit() and not number_b:
            adjacent.append(get_number(engine, i + 1, j + 1))

   if len(adjacent) > 1:
      return functools.reduce(lambda a, b: int(a) * int(b), adjacent)
   
   return 0

for i, ligne in enumerate(engine):
   for j, letter in enumerate(ligne):
      if is_gear(letter):
         sum_ratios = sum_ratios + int(ratio(engine, i, j))

print(sum_ratios)