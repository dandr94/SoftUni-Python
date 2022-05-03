from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard('Foo', 8, )
        self.student.grades_by_subject['Math'] = [5.50, 4.50]

    def test_init_with_default_values(self):
        name = 'Bar'
        school_year = 4
        student = StudentReportCard(name, school_year)
        self.assertEqual(name, student.student_name)
        self.assertEqual(school_year, student.school_year)
        self.assertEqual({}, student.grades_by_subject)

    def test_init_with_non_default_values(self):
        expected_name = 'Foo'
        expected_school_year = 8
        expected_grades_by_subject = {'Math': [5.50, 4.50]}
        self.assertEqual(expected_name, self.student.student_name)
        self.assertEqual(expected_school_year, self.student.school_year)
        self.assertEqual(expected_grades_by_subject, self.student.grades_by_subject)

    def test_student_name_with_empty_string_should_raise_error(self):
        name = ''
        expected_result = 'Student Name cannot be an empty string!'
        with self.assertRaises(ValueError) as ex:
            StudentReportCard(name, 5)

        self.assertEqual(expected_result, str(ex.exception))

    def test_school_year_with_value_above_allowed(self):
        name = 'Foo'
        grade = 12
        expected_result = 'School Year must be between 1 and 12!'
        with self.assertRaises(ValueError) as ex:
            StudentReportCard(name, grade)
        self.assertEqual(expected_result, str(ex.exception))

    def test_school_year_with_value_bellow_allowed(self):
        name = 'Foo'
        grade = 1
        expected_result = 'School Year must be between 1 and 12!'
        with self.assertRaises(ValueError) as ex:
            StudentReportCard(name, grade)
        self.assertEqual(expected_result, str(ex.exception))

    def test_add_grade_method_with_no_existing_subject(self):
        self.student.add_grade('Physics', 4.55)
        expected_result = {'Math': [5.50, 4.50], 'Physics': [4.55]}
        self.assertEqual(expected_result, self.student.grades_by_subject)

    def test_add_grade_method_with_existing_subject(self):
        self.student.add_grade('Math', 4.55)
        expected_result = {'Math': [5.50, 4.50, 4.55]}
        self.assertEqual(expected_result, self.student.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student.add_grade('Physics', 4.55)
        self.student.add_grade('Physics', 4.05)
        result = self.student.average_grade_by_subject()
        expected_result = ''
        for subject, grades in self.student.grades_by_subject.items():
            average_grade = sum(grades) / len(grades)
            expected_result += f"{subject}: {average_grade:.2f}\n"

        self.assertEqual(expected_result.strip(), result)

    def test_average_grade_for_all_subjects(self):
        self.student.add_grade('Physics', 4.55)
        self.student.add_grade('Physics', 5.55)
        self.student.add_grade('Biology', 4.05)
        self.student.add_grade('Biology', 3.05)
        result = self.student.average_grade_for_all_subjects()
        sum_all_grades = 0
        all_count = 0
        for grades in self.student.grades_by_subject.values():
            sum_all_grades += sum(grades)
            all_count += len(grades)
        expected_result = f"Average Grade: {sum_all_grades / all_count :.2f}"
        self.assertEqual(expected_result, result)

    def test_repr_method(self):
        self.student.add_grade('Physics', 4.55)
        self.student.add_grade('Physics', 5.55)
        self.student.add_grade('Biology', 4.05)
        self.student.add_grade('Biology', 3.05)
        average_grade_by_subject_result = ''
        for subject, grades in self.student.grades_by_subject.items():
            average_grade = sum(grades) / len(grades)
            average_grade_by_subject_result += f"{subject}: {average_grade:.2f}\n"

        sum_all_grades = 0
        all_count = 0
        for grades in self.student.grades_by_subject.values():
            sum_all_grades += sum(grades)
            all_count += len(grades)
        average_grade_for_all = f"Average Grade: {sum_all_grades / all_count :.2f}"

        expected_result = f"Name: {self.student.student_name}\n" \
                          f"Year: {self.student.school_year}\n" \
                          f"----------\n" \
                          f"{average_grade_by_subject_result.strip()}\n" \
                          f"----------\n" \
                          f"{average_grade_for_all}"

        self.assertEqual(expected_result, str(self.student))


if __name__ == '__main__':
    main()
