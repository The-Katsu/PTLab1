from Types import DataType


class CharacteristicsCalculator:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def count_excellent_students(self) -> int:
        excellent_students = 0
        for student, subjects in self.data.items():
            if all(score >= 90 for _, score in subjects):
                excellent_students += 1
        return excellent_students