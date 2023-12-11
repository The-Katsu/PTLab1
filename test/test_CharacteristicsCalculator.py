from src.CharacteristicsCalculator import CharacteristicsCalculator
from src.Types import DataType
import pytest


class TestCharacteristicsCalculator:
    @pytest.fixture()
    def input_data(self) -> DataType:
        return {
            "Student1": [("math", 95), ("programming", 92), ("literature", 100)],
            "Student2": [("math", 85), ("programming", 94), ("literature", 88)],
            "Student3": [("math", 91), ("programming", 90), ("literature", 92)],
        }

    def test_count_excellent_students(self, input_data: DataType) -> None:
        calculator = CharacteristicsCalculator(input_data)
        result = calculator.count_excellent_students()
        assert result == 2  # Assuming there are 2 excellent students in the input data

    def test_count_excellent_students_empty_data(self) -> None:
        calculator = CharacteristicsCalculator({})
        result = calculator.count_excellent_students()
        assert result == 0  # No students, so no excellent students

    def test_count_excellent_students_no_excellent_students(self) -> None:
        calculator = CharacteristicsCalculator({"Student1": [("math", 85), ("programming", 88)]})
        result = calculator.count_excellent_students()
        assert result == 0  # No students with all scores >= 90

    def test_count_excellent_students_all_excellent_students(self) -> None:
        calculator = CharacteristicsCalculator({"Student1": [("math", 95), ("programming", 92)]})
        result = calculator.count_excellent_students()
        assert result == 1  # All students are excellent

    def test_count_excellent_students_mixed_scores(self) -> None:
        calculator = CharacteristicsCalculator({"Student1": [("math", 95), ("programming", 92)],
                                                "Student2": [("math", 85), ("programming", 94)]})
        result = calculator.count_excellent_students()
        assert result == 1  # Only Student1 is excellent

    def test_count_excellent_students_negative_scores(self) -> None:
        calculator = CharacteristicsCalculator({"Student1": [("math", -95), ("programming", -92)]})
        result = calculator.count_excellent_students()
        assert result == 0  # No excellent students with negative scores
