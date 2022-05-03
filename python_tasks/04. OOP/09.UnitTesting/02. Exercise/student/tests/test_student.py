from project.student import Student
import unittest


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.student = Student('Yoko')

    def test_init_default(self):
        student_1 = Student('Yoko')
        self.assertEqual(student_1.name, 'Yoko')
        self.assertEqual(student_1.courses, {})

    def test_init_with_none(self):
        student_1 = Student('Yoko', None)
        self.assertEqual(student_1.name, 'Yoko')
        self.assertEqual(student_1.courses, {})

    def test_init_with_course(self):
        student_2 = Student('Foo', {'Math': ['note']})
        self.assertEqual(student_2.name, 'Foo')
        self.assertEqual(student_2.courses, {'Math': ['note']})

    def test_enroll_method_with_same_course_name(self):
        self.student.courses = {'Math': ['Note']}
        test_notes = ['hello', 'bye']
        result = self.student.enroll('Math', test_notes)
        self.assertEqual(result, 'Course already added. Notes have been updated.')
        self.assertEqual(['Note', 'hello', 'bye'], self.student.courses['Math'])

    def test_enroll_with_new_course_default(self):
        result = self.student.enroll('Math', ['Note'])
        self.assertEqual(result, 'Course and course notes have been added.')
        self.assertEqual(self.student.courses, {'Math': ['Note']})

    def test_enroll_with_new_course_and_notes(self):
        result = self.student.enroll('Math', ['Note'], 'Y')
        self.assertEqual(result, 'Course and course notes have been added.')
        self.assertEqual(self.student.courses, {'Math': ['Note']})

    def test_enroll_without_notes(self):
        result = self.student.enroll('Math', ['Note'], 'n')
        self.assertEqual(result, 'Course has been added.')
        self.assertEqual(self.student.courses, {'Math': []})

    def test_add_notes_with_existing_course(self):
        self.student.courses = {'Math': ['Note']}
        res = self.student.add_notes('Math', 'hello')
        self.assertEqual(res, 'Notes have been updated')
        self.assertEqual(self.student.courses, {'Math': ['Note', 'hello']})

    def test_add_notes_without_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Math', ['Note'])

        self.assertEqual(str(ex.exception), 'Cannot add notes. Course not found.')

    def test_leave_course_with_existing_course(self):
        self.student.courses = {'Math': ['Note']}
        res = self.student.leave_course('Math')
        self.assertEqual(res, 'Course has been removed')
        self.assertEqual(self.student.courses, {})

    def test_leave_course_with_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Math')

        self.assertEqual(str(ex.exception), 'Cannot remove course. Course not found.')


if __name__ == '__main__':
    unittest.main()
