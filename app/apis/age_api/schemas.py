from pydantic import BaseModel

class AgeGroup(BaseModel):
    min_age: int
    max_age: int

    def to_dict(self):
        return {
            "min_age":self.min_age,
            "max_age":self.max_age
        }