from typing import Dict, List, Tuple


class StudentCalculator:
    @staticmethod
    def count_excellent_students(data: Dict[str, List[Tuple[str, int]]]) \
            -> int:
        excellent_students_count = 0

        for student, scores in data.items():
            is_excellent = all(score >= 90 for _, score in scores)
            if is_excellent:
                excellent_students_count += 1

        return excellent_students_count
