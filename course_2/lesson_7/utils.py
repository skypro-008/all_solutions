import json

from config import STUDENTS_PATH, PROFESSIONS_PATH


def load_students():
    """ Загружает студентов из файла"""
    with open(STUDENTS_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_professions():
    """ Загружает профессии из файла"""
    with open(PROFESSIONS_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_student_by_pk(pk):
    """ Получает студента по его номеру"""
    students = load_students()
    for student in students:
        if student.get("pk") == pk:
            return student


def get_profession_by_title(title):
    """ Получает профессию по ее названию"""
    professions = load_professions()
    for profession in professions:
        if profession.get("title") == title.title():
            return profession


def check_fitness(student, profession):
    """ Находит соответствие между студентами и профессией"""

    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])

    has_skills = student_skills.intersection(profession_skills)
    lacks_skills = profession_skills.difference(has_skills)

    has_percent = round(len(has_skills) / len(profession_skills) * 100)

    return {
        "has": list(has_skills),
        "lacks": list(lacks_skills),
        "fit_percent": has_percent,
    }

    return has_skills, lack_skills, has_percent

