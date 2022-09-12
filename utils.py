import json

class Candidates_Choice:

    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"Candidates_Choice({self.path})"

    def load_candidates(self):
        """
        Возвращает список всех кандидатов
        """
        with open(self.path) as file:
            data = json.load(file)
        return data

    def get_candidate(self, cid):
        """
        Возвращает одного кандидата по его id
        """
        candidates = self.load_candidates()
        for candidate in candidates:
            if candidate['id'] == cid:
                return candidate

    def get_all_candidates(self):
        """
        Возвращает всех кандидатов
        """
        candidates = self.load_candidates()
        return candidates

    def get_candidates_by_name(self, name):
        """
        Возвращает кандидатов по имени
        """
        candidates = self.load_candidates()
        name = name.lower()
        matching_candidates = [candidate for candidate in candidates if name in candidate["name"].lower()]
        return matching_candidates

    def get_candidates_by_skill(self, skill):
        """
        Возвращает кандидатов по навыку
        """
        candidates = self.load_candidates()
        skill = skill.lower()

        matching_candidates = []

        for candidate in candidates:
            candidate_skills = candidate['skills'].lower().split(", ")
            if skill in candidate_skills:
                matching_candidates.append(candidate)

        return matching_candidates







