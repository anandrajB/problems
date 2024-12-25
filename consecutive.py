def consecutive(nums):
    max_count = count = 0
    for item in nums:
        count = count + 1 if item == 0 else 0
        max_count = max(max_count, count)
    return max_count


ds = consecutive([0, 34, 1, 42, 0, 0, 0, 323, 54])
print(ds)
