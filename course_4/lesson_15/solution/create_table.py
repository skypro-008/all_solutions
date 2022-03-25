import sqlite3


# 1 нормальная форма — убираем столбцы color1 и color2
con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "CREATE TABLE colors(" \
        "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
        "name VARCHAR(30))"
cursor.execute(query)
con.close()

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "INSERT INTO colors (name) " \
        "SELECT color1 FROM animals"
cursor.execute(query)
con.close()

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "CREATE TABLE animal_colors(" \
        "animal_id INT," \
        "color_id INT)"
cursor.execute(query)
con.close()

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "insert into animal_colors" \
        "select animals.\"index\", colors.id from animals" \
        "join colors on color1 = colors.name "
cursor.execute(query)
con.close()

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "insert into animal_colors" \
        "select animals.\"index\", colors.id from animals" \
        "join colors on color2 = colors.name "
cursor.execute(query)
con.close()

# 2 нормальная форма — данные по outcome выносим в отдельную таблицу
# (столбцы outcome_subtype, outcome_type, outcome_month, outcome_year)

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "CREATE TABLE outcomes(" \
        "outcome_id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "outcome_subtype VARCHAR(50), " \
        "outcome_type VARCHAR(30)," \
        "outcome_month INT," \
        "outcome_year INT)"
cursor.execute(query)
con.close()

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "INSERT INTO outcomes (outcome_subtype, outcome_type, outcome_month, outcome_year)" \
        "select outcome_subtype, outcome_type, outcome_month, outcome_year from animals " \
        "group by outcome_subtype, outcome_type, outcome_month, outcome_year"
cursor.execute(query)
con.close()

# 3 нормальная форма. Создаем словари для animal_type, breed
con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "CREATE TABLE animal_types(" \
        "id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "name varchar(30))"
cursor.execute(query)
con.close()

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "INSERT INTO animal_types(name) " \
        "SELECT distinct(animal_type) FROM animals "
cursor.execute(query)
con.close()

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "CREATE TABLE breed(" \
        "id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "name varchar(30))"
cursor.execute(query)
con.close()

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "INSERT INTO breed(name) " \
        "SELECT distinct(breed) FROM animals"
cursor.execute(query)
con.close()

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "CREATE TABLE animals_fin(" \
        "id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "age_upon_outcome varchar(30)," \
        "animal_id varchar(30)," \
        "type_id INT," \
        "name VARCHAR(50)," \
        "breed_id INT," \
        "date_of_birth DATE," \
        "outcome_id INT)"
cursor.execute(query)
con.close()

con = sqlite3.connect('animals.db')
cursor = con.cursor()
query = "INSERT INTO animals_fin" \
        "SELECT \"index\", age_upon_outcome, animal_id, animal_types.id," \
        "animals.name, breed.id, date_of_birth, outcomes.outcome_id" \
        "FROM animals" \
        "LEFT JOIN animal_types ON animal_type = animal_types.name" \
        "LEFT JOIN breed ON animals.breed = breed.name" \
        "LEFT JOIN outcomes ON animals.outcome_subtype = outcomes.outcome_subtype " \
        "AND animals.outcome_type = outcomes.outcome_type " \
        "AND animals.outcome_month = outcomes.outcome_month " \
        "AND animals.outcome_year = outcomes.outcome_year "
cursor.execute(query)
con.close()