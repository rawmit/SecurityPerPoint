
class Entity:
    id = None
    score = None
    active = None
    lastcheck = None

    def __init__(self, id, score, active, lastcheck):
        self.id = id
        self.score = score
        self.active = active
        self.lastcheck = lastcheck