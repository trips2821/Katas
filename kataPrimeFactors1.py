from builtins import staticmethod


class PrimeFactors:

    def __init__(self):
        pass

    @staticmethod
    def generate(number):
        primes = []
        divisor = 2
        while number > 1:
            while number % divisor == 0:
                primes.append(divisor)
                number /= divisor
            divisor += 1
        if number > 1:
            primes.append(number)
        return primes

