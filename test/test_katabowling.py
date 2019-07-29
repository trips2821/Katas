import pytest

from katabowling import KataBowling


class TestKataBowling:
    @pytest.fixture(autouse=True)
    def initialize(self):
        self.g = KataBowling()

    def roll_many(self, pins, n):
        for i in range(0, n):
            self.g.roll(pins)

    def roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)

    def roll_strike(self):
        self.g.roll(10)

    def test_gutter_game(self):
        self.roll_many(pins=0, n=20)

        assert self.g.score == 0

    def test_all_ones(self):
        self.roll_many(pins=1, n=20)

        assert self.g.score == 20

    def test_one_spare(self):
        self.roll_spare()
        self.g.roll(3)
        self.roll_many(0, 17)

        assert self.g.score == 16

    def test_one_strike(self):
        self.roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self.roll_many(0, 17)

        assert self.g.score == 24

    def test_perfect_game(self):
        self.roll_many(10, 12)

        assert self.g.score == 300
