'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import math

def solution(num1, num2, limit):

    num_mults_of_num1 = int((limit - 1) / num1)
    sum_mults_of_num1 = int(num1 * (num_mults_of_num1 * (num_mults_of_num1 + 1)) / 2)

    num_mults_of_num2 = int((limit - 1) / num2)
    sum_mults_of_num2 = int(num2 * (num_mults_of_num2 * (num_mults_of_num2 + 1)) / 2)

    lcm_of_nums = (num1 * num2) / math.gcd(num1, num2)

    num_mults_of_lcm_of_nums = int((limit - 1) / lcm_of_nums)
    sum_mults_of_lcm_of_nums = int(lcm_of_nums * (num_mults_of_lcm_of_nums * (num_mults_of_lcm_of_nums + 1)) / 2)

    sum_unique_mults_of_nums = (sum_mults_of_num1 + sum_mults_of_num2) - sum_mults_of_lcm_of_nums

    return sum_unique_mults_of_nums

print(solution(3, 5, 1000))
