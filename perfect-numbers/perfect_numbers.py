import math

def classify(number):
    if number < 1:
        raise ValueError('Wrong number')
    aliquot_sum = sum([i for i in range(1, number) if not number % i])
    result = 'perfect' if aliquot_sum == number else 'abundant'
    return 'deficient' if aliquot_sum < number else result

# def classify(number):
#     if number <= 0:
#         raise ValueError('number must be > 0')
#
#     aliquot = sum(set(
#         factor for i in range(1, int(number ** 0.5) + 1) if number % i == 0
#         for factor in (i, number//i)
#     )) - number
#
#     if aliquot > number:
#         return 'abundant'
#
#     elif aliquot < number:
#         return 'deficient'
#
#     return 'perfect'