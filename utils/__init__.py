import math
import uuid
import random


def random_sub():
    nums = []
    j = 0
    while True:
        num = uuid.uuid4().int
        print(f'{j} => {num} => D: {int(math.log10(num)) + 1}')
        dup = False
        x = 0
        for i in nums:
            if i == num:
                dup = True
                print(f"index = {x}, number = {i}")
            x += 1
        if dup:
            break
        j += 1
        nums.append(num)


def random_digits(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    nums = []
    while True:
        ran = random.randint(lower, upper)
        print(ran)
        if ran in nums:
            print(f"Attempts => {len(nums)}")
            break
        nums.append(ran)


if __name__ == '__main__':
    random_digits(5)
