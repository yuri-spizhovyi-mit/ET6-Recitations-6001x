def has22(nums):
    result = 0
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            result += 1
    if result >= 1:
        return True
    else:
        return False


print(has22([1, 2, 2]))
