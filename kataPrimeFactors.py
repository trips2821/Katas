
class PrimeFactors:

    @staticmethod
    def generate(number):
        primes = []

        divisor = 2
        while number > 1:
            while number % divisor == 0:
                primes.append(divisor)
                number /= divisor
            divisor += 1

        return primes

