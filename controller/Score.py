from models.Result import Result


class ScoreContext:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._score = {"wins": 0, "losses": 0, "ties": 0}
        return cls._instance

    def update_score(self, result: Result):
        if result == Result.WIN:
            self._score["wins"] += 1
        elif result == Result.LOSE:
            self._score["losses"] += 1
        else:
            self._score["ties"] += 1

    def get_score(self):
        return self._score.copy()
