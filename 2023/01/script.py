# Advent Of Code 2023
# Day 1: Trebuchet
# By Vincweb

import re

# Spécifiez le chemin du fichier que vous souhaitez lire
input_file = './input.txt'
regex_number = '(one|two|three|four|five|six|seven|eight|nine)'
match_number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
fusion_case = '(oneight|twone|threeight|fiveight|sevenine|eightwo|eighthree|nineight)'
fusion_number = {
    "oneight": "oneeight",
    "twone": "twoone",
    "threeight": "threeeight",
    "fiveight": "fiveeight",
    "sevenine": "sevennine",
    "eightwo": "eighttwo",
    "eighthree": "eightthree",
    "nineight": "nineeight"
}

sum = 0

# Ouvrez le fichier en mode lecture
with open(input_file, 'r') as fichier:
    # Lisez chaque ligne du fichier
    for ligne in fichier:

        # Utilisez une expression régulière pour effectuer le remplacement
        fix_chaine = re.sub(fusion_case, lambda x: str(fusion_number[x.group()]), ligne)

        nouvelle_chaine = re.sub(regex_number, lambda x: str(match_number[x.group()]), fix_chaine)

        # Récupérez seulement les nombres
        nombres = re.sub(r'\D', '', nouvelle_chaine)

        # Récupérez le premier nombre de la ligne
        premier_caractere = nombres[0]
        
        # Récupérez le dernier nombre de la ligne
        dernier_caractere = nombres[-1]

        # Assemble le chiffre
        chiffre = int(premier_caractere + dernier_caractere)

        sum = sum + chiffre

print(sum)
