'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import functools

def gcd(*numbers):
    def helper(num1, num2):
        large, small = (num1, num2) if num1 > num2 else (num2, num1)
        while small > 0:
            remainder = large % small
            if remainder == 0:
                break
            large, small = small, remainder
        return small
    return functools.reduce(helper, numbers)

def lcm(*numbers):
    def helper(num1, num2):
        return int(num1 * num2 / gcd(num1, num2)) if num1 > 0 and num2 > 0 else 0
    return int(functools.reduce(helper, numbers))

def correct_sum_mults(limit, *numbers):
    numbers = list(numbers)
    result = 0
    for i in range(1, limit):
        for num in numbers:
            if i % num == 0:
                result += i
                break
    return result

def sum_mults_single_num(limit, num):
    num_mults = (int((limit - 1) / num))
    return (int(num * (num_mults * (num_mults + 1) / 2)))

def sum_dupes_double_num(limit, num1, num2):
    return (sum_mults_single_num(limit, lcm(num1, num2)))

def sum_mults_double_num(limit, num1, num2):
    return (sum_mults_single_num(limit, num1) +
            sum_mults_single_num(limit, num2) -
            sum_dupes_double_num(limit, num1, num2))

def sum_dupes_triple_num(limit, num1, num2, num3):
    return (sum_dupes_double_num(limit, num1, num2) +
            sum_dupes_double_num(limit, num1, num3) +
            sum_dupes_double_num(limit, num2, num3) -
            sum_mults_single_num(limit, lcm(num1, num2, num3)))

def sum_mults_triple_num(limit, num1, num2, num3):
    return (sum_mults_single_num(limit, num1) +
            sum_mults_single_num(limit, num2) +
            sum_mults_single_num(limit, num3) -
            sum_dupes_triple_num(limit, num1, num2, num3))

# ------------------
# TODO FIXME - @ZACH
# ------------------
# Consolidate the above functions into a generic sum_mults() function
# and a generic sum_dupes() function. Both functions should take a
# limit argument as well as an arbitrary amount of number arguments.
# ------------------

def solution():
    limit = 1000
    result = sum_mults_double_num(limit, 3, 5)
    return result

print(solution())

# print("sum_mults_single_num(61, 3) = "       + str(sum_mults_single_num(61, 3)))
# print("sum_mults_single_num(61, 4) = "       + str(sum_mults_single_num(61, 4)))
# print("sum_mults_single_num(61, 5) = "       + str(sum_mults_single_num(61, 5)))

# print("sum_dupes_double_num(61, 3, 4) = "    + str(sum_dupes_double_num(61, 3, 4)))
# print("sum_dupes_double_num(61, 3, 5) = "    + str(sum_dupes_double_num(61, 3, 5)))
# print("sum_dupes_double_num(61, 4, 5) = "    + str(sum_dupes_double_num(61, 4, 5)))

# print("sum_mults_double_num(61, 3, 4) = "    + str(sum_mults_double_num(61, 3, 4)))
# print("sum_mults_double_num(61, 3, 5) = "    + str(sum_mults_double_num(61, 3, 5)))
# print("sum_mults_double_num(61, 4, 5) = "    + str(sum_mults_double_num(61, 4, 5)))

# print("sum_dupes_triple_num(61, 3, 4, 5) = " + str(sum_dupes_triple_num(61, 3, 4, 5)))

# print("sum_mults_triple_num(61, 3, 4, 5) = " + str(sum_mults_triple_num(61, 3, 4, 5)))

# print("correct_sum_mults(61, 3, 4, 5) = " + str(correct_sum_mults(61, 3, 4, 5)))

# 12 24 36 48 60
# 15 30 45 60
# 20 40 60

# 12 15 20 24 30 36 40 45 48 60

#        3  4  5  6     8  9 10
#    12       15 16    18    20
# 21       24 25    27 28    30
#    32 33    35 36       39 40
#    42    44 45       48    50
# 51 52    54 55 56 57       60
