import sqlite3
import json
from flask import Flask, render_template, request


def main():
    app = Flask(__name__)

    @app.route('/animals/<int:idx>')
    def animals(idx):
        con = sqlite3.connect('animal.db')
        cursor = con.cursor()
        query = "SELECT age_upon_outcome, animal_id, animal_types.name, breed.name, date_of_birth FROM animals_fin " \
                "LEFT JOIN breed ON animals_fin.breed_id = breed.id " \
                "LEFT JOIN animal_types ON animals_fin.type_id = animal_types.id " \
                f"WHERE animals_fin.id = {idx}"
        cursor.execute(query)
        result = cursor.fetchall()
        con.close()
        if len(result) == 1:
            line = result[0]
            result_dict = {
                "age_upon_outcome": line[0],
                "animal_id": line[1],
                "animal_type": line[2],
                "breed": line[3],
                "date_of_birth": line[4]
            }
        else:
            result_dict = {}
        return json.dumps(result_dict)

    app.run()


if __name__ == '__main__':
    main()






































# import pandas as pd
# import sqlite3
# def print_hi(name):
#     df = pd.DataFrame(columns=['name','pokedex_number','abilities','typing','hp','attack','defense',
#                                'special_attack','special_defense','speed','height','weight','genus',
#                                'gen_introduced','female_rate','genderless','baby_pokemon','legendary',
#                                'mythical','is_default','forms_switchable','base_experience',
#                                'capture_rate','egg_groups','egg_cycles','base_happiness','can_evolve',
#                                'evolves_from','primary_color','shape','number_pokemon_with_typing',
#                                'normal_attack_effectiveness','fire_attack_effectiveness','water_attack_effectiveness',
#                                'electric_attack_effectiveness','grass_attack_effectiveness','ice_attack_effectiveness',
#                                'fighting_attack_effectiveness','poison_attack_effectiveness','ground_attack_effectiveness',
#                                'fly_attack_effectiveness','psychic_attack_effectiveness','bug_attack_effectiveness',
#                                'rock_attack_effectiveness','ghost_attack_effectiveness','dragon_attack_effectiveness',
#                                'dark_attack_effectiveness','steel_attack_effectiveness','fairy_attack_effectiveness'
# ])
#     j = 0
#     with open(r"C:\Users\sand1\Downloads\pokemon.csv", encoding='utf-8') as f:
#         for line in f:
#             if 'pokedex_number' not in line:
#                 print(line)
#                 line_list = []
#                 checkline = True
#                 start = 0
#                 for i, char in enumerate(line):
#                     if char == ',' and checkline:
#                         if line[i-1] == ',':
#                             line_list.append('None')
#                         else:
#                             line_list.append(line[start:i].replace('"', ''))
#                         start = i+1
#                     if char == '"':
#                         checkline = not checkline
#                 line_list.append(line[start:-1])
#                 print(line_list[0])
#                 df.loc[i] = line_list
#                 j += 1
#     con = sqlite3.connect('pokemon.db')
#     print(j)
#     df.to_sql('pokemon',con=con, index=False)
# if __name__ == '__main__':
#     print_hi('PyCharm')


