import json


def load_candidates():
    """ Загружает кандидатов из файла, возвращает в виде словаря"""
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)

    return candidates


def get_candidates_all():
    """ Возввращает полный список кандидатов"""
    return load_candidates()


def get_candidates_by_skill(skill):
    """ Возвращает список кандидатов по навыку"""
    candidates = load_candidates()
    skilled_candidates = []
    skill_lower = skill.lower()

    for candidate in candidates:
        candidate_skills = candidate["skills"].lower().split(", ")
        if skill_lower in candidate_skills:
            skilled_candidates.append(candidate)

    return skilled_candidates


def get_candidate_by_id(uid):
    """ Возвращает одного кандидата по его id """
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate


def build_preformnatted_list(candidates):
    """ Создает список из полученных кандидатов"""
    page_content = ""

    for candidate in candidates:
        page_content += candidate["name"]+"\n"
        page_content += candidate["position"]+"\n"
        page_content += candidate["skills"]+"\n"
        page_content += "\n"

    return "<pre>"+page_content+"</pre>"


print(__name__)
