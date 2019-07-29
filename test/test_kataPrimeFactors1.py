import pytest

from kataPrimeFactors1 import PrimeFactors


class TestKataPrimeFactors:
    @pytest.fixture(autouse=True)
    def initialize(self):
        pass

    def test_one(self):
        assert PrimeFactors.generate(1) == []

    def test_two(self):
        assert PrimeFactors.generate(2) == [2, ]

    def test_three(self):
        assert PrimeFactors.generate(3) == [3, ]

    def test_four(self):
        assert PrimeFactors.generate(4) == [2, 2]

    def test_six(self):
        assert PrimeFactors.generate(6) == [2, 3]

    def test_eight(self):
        assert PrimeFactors.generate(8) == [2, 2, 2]

    def test_nine(self):
        assert PrimeFactors.generate(9) == [3, 3]
