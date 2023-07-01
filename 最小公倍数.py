def lcm(nums:list[int]) -> int:
    from math import gcd
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    lcm_value = nums[0] * nums[1] // gcd(nums[0], nums[1])
    for num in nums[2:]:
        lcm_value = lcm_value * num // gcd(lcm_value, num)
    while lcm_value > 1000:
        lcm_value = lcm_value // 2
    return lcm_value