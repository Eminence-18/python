def find_min(nums):
    if not nums:
        return None

    min_so_far = float("inf")
    for num in nums:
        min_so_far = min(min_so_far, num)

    return min_so_far