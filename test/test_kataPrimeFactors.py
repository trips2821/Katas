import pytest

from kataPrimeFactors import PrimeFactors


class TestKataPrimeFactors:
    @pytest.fixture(autouse=True)
    def initialize(self):
        pass

    def testOne(self):
        assert PrimeFactors.generate(1) == []

    def testTwo(self):
        assert PrimeFactors.generate(2) == [2, ]

    def testThree(self):
        assert PrimeFactors.generate(3) == [3, ]

    def testFour(self):
        assert PrimeFactors.generate(4) == [2, 2]

    def testFive(self):
        assert PrimeFactors.generate(5) == [5, ]

    def testSix(self):
        assert PrimeFactors.generate(6) == [2, 3]

    def testEight(self):
        assert PrimeFactors.generate(8) == [2, 2, 2]

    def testNine(self):
        assert PrimeFactors.generate(9) == [3, 3]
