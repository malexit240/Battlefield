from unittest import TestCase

from units import Soldier
from local_random import R


class Tests_for_Soldier_class(TestCase):

    def setUp(self):
        self.soldier = Soldier(100, 0)
        R.seed(0)

    def test_attack_probability_in_0_1(self):
        self.soldier.experience = 50

        attack_probability = self.soldier.attack_probability
        self.assertTrue(attack_probability >= 0 and attack_probability <= 1)

    def test_experience_not_more_50(self):
        self.soldier.experience = 100

        self.assertEqual(self.soldier.experience, 50)

    def test_experience_not_less_0(self):
        self.soldier.experience = -100

        self.assertEqual(self.soldier.experience, 0)

    def test_damage_inflicte(self):
        self.soldier.damage_inflicte(1)

        self.assertEqual(self.soldier.health, 99)

    def test_hit_return_True(self):
        self.assertEqual(self.soldier.hit, True)

    def test_beat_returns_damage(self):
        other_soldier = Soldier(100, 0)
        self.soldier.experience = 50

        self.assertEqual(self.soldier.beat(other_soldier), self.soldier.damage)

    def test_experiance_was_increase(self):
        other_soldier = Soldier(100, 0)
        self.soldier.beat(other_soldier)

        self.assertEqual(self.soldier.experience, 1)
