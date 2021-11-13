class ExercisePlan:
    ID = 1

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()

    @staticmethod
    def get_next_id():
        res = ExercisePlan.ID
        ExercisePlan.ID += 1
        return res

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        minutes = hours * 60
        return cls(trainer_id, equipment_id, minutes)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
