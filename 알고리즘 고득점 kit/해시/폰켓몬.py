import math
def solution(nums):
    answer = 0
    numSet = set(nums)
    half_length = math.floor(len(nums) / 2)

    return min(len(numSet), half_length)