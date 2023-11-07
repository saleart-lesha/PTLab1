import pytest
from src.StudentCalculator import StudentCalculator


class TestStudentCalculator:
    @pytest.fixture
    def sample_data(self):
        data = {
            "Иванов Иван Иванович": [("математика", 67),
                                     ("литература", 100),
                                     ("программирование", 91)],
            "Петров Петр Петрович": [("математика", 78),
                                     ("химия", 87),
                                     ("социология", 91)],
            "Сидоров Сидор Сидорович": [("математика", 95),
                                        ("физика", 92),
                                        ("химия", 94)]
        }
        return data

    def test_count_excellent_students(self, sample_data):
        excellent_count = \
            StudentCalculator.count_excellent_students(sample_data)
        assert excellent_count == 1

    def test_count_excellent_students_empty_data(self):
        empty_data = {}
        excellent_count = \
            StudentCalculator.count_excellent_students(empty_data)
        assert excellent_count == 0

    def test_count_excellent_students_no_excellent_students(self):
        data = {
            "Иванов Иван Иванович": [("математика", 67), ("литература", 85)],
            "Петров Петр Петрович": [("математика", 78), ("химия", 87)]
        }
        excellent_count = StudentCalculator.count_excellent_students(data)
        assert excellent_count == 0

    def test_count_excellent_students_all_excellent_students(self):
        data = {
            "Иванов Иван Иванович": [("математика", 95), ("литература", 100)],
            "Петров Петр Петрович": [("математика", 98), ("химия", 97)]
        }
        excellent_count = StudentCalculator.count_excellent_students(data)
        assert excellent_count == len(data)
