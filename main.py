from flask import Flask, render_template

from utils import Candidates_Choice

app = Flask(__name__)

candidates_choice = Candidates_Choice("candidates.json")

@app.route('/')

def page_index():

    candidates = candidates_choice.get_all_candidates()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:can_id>')

def page_single_candidate(can_id):
    candidate = candidates_choice.get_candidate(can_id)

    return render_template('single.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def page_search_candidate(candidate_name):
    candidates = candidates_choice.get_candidates_by_name(candidate_name)
    candidates_len = len(candidates)

    return render_template('search.html', candidates=candidates, candidates_len=candidates_len)

@app.route('/skill/<skill_name>')
def page_skill_candidate(skill_name):
    candidates = candidates_choice.get_candidates_by_skill(skill_name)
    candidates_len = len(candidates)

    return render_template('skill.html', candidates=candidates, candidates_len=candidates_len, skill_name=skill_name)

if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)




