from flask import Flask, request, render_template

from classes.candidate_manager import CandidateManager
from config import PATH, LIMIT

app = Flask(__name__)
candidate_manager = CandidateManager(PATH)

str
@app.route('/')
def page_index():
    """ Главная страничка со всеми кандидатами """
    candidates = candidate_manager.load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route('/candidates/<int:candidate_id>')
def page_candidate(candidate_id):
    """ Страничка одного кандидата """
    candidate = candidate_manager.get_candidate_by_id(candidate_id)

    if not candidate:
        return "Кандидат не найден"

    return render_template("single.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def page_search(candidate_name):
    """ Поиск кандидатов по имени """
    candidates = candidate_manager.get_candidates_by_name(candidate_name)
    candidates_count = len(candidates)
    return render_template("search.html", candidates=candidates, candidates_count=candidates_count)


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    """ Список кандидатов с конкретным навыком """
    candidates = candidate_manager.get_candidates_by_skill(skill_name)
    candidates_count = len(candidates)
    return render_template("skill.html", candidates=candidates, candidates_count=candidates_count)


app.run()
