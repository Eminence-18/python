def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        max_so_far = max(max_so_far, num)
    return max_so_far
