from project.library import Library

from unittest import TestCase, main


class LibraryTests(TestCase):
    def setUp(self) -> None:
        self.library = Library('Sofia')
        self.library.books_by_authors['Jacob'] = ['Empty woods']
        self.library.readers['Pesho'] = []

    def test_if_init_properly_returns_correct_values_default(self):
        library = Library('Sofia')
        self.assertEqual('Sofia', library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_empty_string_as_value_for_name_should_raise_error(self):
        with self.assertRaises(Exception) as ex:
            Library('')
        self.assertEqual('Name cannot be empty string!', str(ex.exception))

    def test_add_book_method_with_non_existing_author(self):
        expected_result_empty = {'Jacob': ['Empty woods'], 'Mike': ['Wrong doings']}
        self.library.add_book('Mike', 'Wrong doings')
        self.assertEqual(expected_result_empty, self.library.books_by_authors)

    def test_add_book_method_with_existing_author(self):
        self.library.add_book('Jacob', 'Criminal minds')
        expected_result = {'Jacob': ['Empty woods', 'Criminal minds']}
        self.assertEqual(expected_result, self.library.books_by_authors)

    def test_add_non_existing_reader(self):
        self.library.add_reader('Gosho')
        expected_result = {'Gosho': [], 'Pesho': []}
        self.assertEqual(expected_result, self.library.readers)

    def test_add_existing_reader(self):
        name = 'Pesho'
        result = self.library.add_reader(name)
        self.assertEqual(f"{name} is already registered in the {self.library.name} library.", result)

    def test_rent_book_if_reader_is_not_registered(self):
        reader_name = 'Mitko'
        author = 'Foo'
        title = 'Bar'
        result = self.library.rent_book(reader_name, author, title)
        expected_result = f"{reader_name} is not registered in the {self.library.name} Library."
        self.assertEqual(expected_result, result)

    def test_rent_book_with_non_existing_author(self):
        reader_name = 'Pesho'
        author = 'Foo'
        title = 'Bar'
        result = self.library.rent_book(reader_name, author, title)
        expected_result = f"{self.library.name} Library does not have any {author}'s books."
        self.assertEqual(expected_result, result)

    def test_rent_book_with_wrong_title(self):
        reader_name = 'Pesho'
        author = 'Jacob'
        title = 'Bar'
        result = self.library.rent_book(reader_name, author, title)
        expected_result = f"""{self.library.name} Library does not have {author}'s "{title}"."""
        self.assertEqual(expected_result, result)

    def test_rent_book_properly(self):
        reader_name = 'Pesho'
        author = 'Jacob'
        title = 'Empty woods'
        expected_result_reader = {'Pesho': [{'Jacob': 'Empty woods'}]}
        self.library.rent_book(reader_name, author, title)
        self.assertEqual(expected_result_reader, self.library.readers)
        expected_result_author = {'Jacob': []}
        self.assertEqual(expected_result_author, self.library.books_by_authors)


if __name__ == '__main__':
    main()
