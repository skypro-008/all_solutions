import utils

# Получаем данные про студента
print("Введите номер студента")
student_id = int(input())
student = utils.get_student_by_pk(student_id)

if not student:
    print("У нас нет такого студента")
    quit()

# Собираем информацию о знаниях и изучаемых студента
student_name = student["full_name"]
student_skills = " ".join(student["skills"])
student_learns = " ".join(student["learns"])

# Выводим информацию о знаниях и изучаемых студента
print(f"Студент {student_name}")
print(f"Знает {student_skills}")

# Получаем данные про профессию
print("Выберите специальность для оценки студента Jane Snake")
profession_title = input()
profession = utils.get_profession_by_title(profession_title)

if not profession:
    print("У нас нет такой профессии")
    quit()

# Получаем сопоставление
fitness = utils.check_fitness(student, profession)

# Вытаскиваем данные из полученного словаря
fit_percent = fitness["fit_percent"]
has = fitness["has"]
lacks = fitness["lacks"]
useless = fitness["useless"]

# Выводим результаты
print(f"Пригодность {fit_percent}%")
print(f"Студент знает {' '.join(has)}")
print(f"Студент не знает {' '.join(lacks)}")
