from project.team import Team
from unittest import main, TestCase


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team('Mitko')
        self.team.members = {'Hary': 5}

    def test_init_with_default_values(self):
        name = 'Har'
        team = Team(name)
        self.assertEqual(name, team.name)
        self.assertEqual({}, team.members)

    def test_init_with_non_default_values(self):
        expected_name = 'Mitko'
        expected_members = {'Hary': 5}
        self.assertEqual(expected_name, self.team.name)
        self.assertEqual(expected_members, self.team.members)

    def test_init_name_with_numbers_should_raise_error(self):
        name = 'maybe1'
        with self.assertRaises(ValueError) as ex:
            Team(name)

        expected_result = 'Team Name can contain only letters!'
        self.assertEqual(expected_result, str(ex.exception))

    def test_add_member_method(self):
        values = {'Hero': 4, 'Barney': 7}
        expected_dict_result = {'Hary': 5,
                                'Hero': 4,
                                'Barney': 7}
        expected_str_result = 'Successfully added: Hero, Barney'
        result = self.team.add_member(**values)
        self.assertEqual(expected_dict_result, self.team.members)
        self.assertEqual(expected_str_result, result)

    def test_remove_member_without_existing_member(self):
        name = 'Barney'
        expected_result = f'Member with name {name} does not exist'
        result = self.team.remove_member(name)
        self.assertEqual(expected_result, result)

    def test_remove_member_with_existing_one(self):
        name = 'Hary'
        expected_str_result = f'Member {name} removed'
        expected_dict_result = {}
        result = self.team.remove_member(name)
        self.assertEqual(expected_str_result, result)
        self.assertEqual(expected_dict_result, self.team.members)

    def test_gt_method_true(self):
        team_2 = Team('Her')
        values = {'Hero': 4, 'Barney': 7}
        self.team.add_member(**values)
        team_2.add_member(**values)
        expected_result = True
        self.assertEqual(expected_result, self.team > team_2)

    def test_gt_method_false(self):
        team_2 = Team('Her')
        values = {'Hero': 4, 'Barney': 7}
        team_2.add_member(**values)
        expected_result = False
        self.assertEqual(expected_result, self.team > team_2)

    def test_len_method(self):
        result = len(self.team)
        expected_result = 1
        self.assertEqual(expected_result, result)

    def test_add_method(self):
        team_2 = Team('Hero')
        values = {'Hero': 4, 'Barney': 7}
        team_2.add_member(**values)
        new_team = self.team + team_2
        expected_name = 'MitkoHero'
        expected_members = {'Hary': 5,
                            'Hero': 4,
                            'Barney': 7}

        self.assertEqual(expected_name, new_team.name)
        self.assertEqual(expected_members, new_team.members)

    def test_str_method(self):
        values = {'Hero': 5, 'Shorty': 7}
        self.team.add_member(**values)
        expected_result = f'Team name: Mitko\n' \
                          f'Member: Shorty - 7-years old\n' \
                          f'Member: Hary - 5-years old\n' \
                          f'Member: Hero - 5-years old'

        self.assertEqual(expected_result, str(self.team))


if __name__ == '__main__':
    main()
