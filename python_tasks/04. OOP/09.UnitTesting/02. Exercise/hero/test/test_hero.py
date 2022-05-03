from project.hero import Hero
import unittest


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Yoko', 5, 50, 5)
        self.enemy_hero = Hero('Blob', 2, 50, 1)

    def test_init_properly_holding_all_attributes(self):
        hero = Hero('Yoko', 5, 50, 5)
        self.assertEqual(hero.username, 'Yoko')
        self.assertEqual(hero.level, 5)
        self.assertEqual(hero.health, 50)
        self.assertEqual(hero.damage, 5)

    def test_battle_with_same_name(self):
        self.enemy_hero.username = 'Yoko'
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ex.exception), 'You cannot fight yourself')

    def test_battle_if_hero_have_zero_or_less_hp(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_if_enemy_hero_have_zero_or_less_hp(self):
        self.enemy_hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ex.exception), f"You cannot fight {self.enemy_hero.username}. He needs to rest")

    def test_draw_battle(self):
        self.hero.damage = 500
        self.enemy_hero.damage = 500

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(result, 'Draw')

    def test_hero_win_battle(self):
        self.hero.level = 50
        self.hero.health = 1000
        self.hero.damage = 500
        # damage = 25_000

        self.hero.battle(self.enemy_hero)
        self.assertEqual(self.enemy_hero.health, -24_950)
        self.assertEqual(self.hero.health, 1003)
        self.assertEqual(self.hero.level, 51)
        self.assertEqual(self.hero.damage, 505)

        self.enemy_hero.health = 5
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(result, 'You win')

    def test_hero_lose_battle(self):
        self.enemy_hero.level = 50
        self.enemy_hero.health = 1000
        self.enemy_hero.damage = 500
        # damage = 25_000

        self.hero.battle(self.enemy_hero)
        self.assertEqual(self.hero.health, -24_950)
        self.assertEqual(self.enemy_hero.level, 51)
        self.assertEqual(self.enemy_hero.health, 980)
        self.assertEqual(self.enemy_hero.damage, 505)
        self.hero.health = 5
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(result, 'You lose')

    def test_if_str_properly_returns_info(self):
        result = str(self.hero)
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
