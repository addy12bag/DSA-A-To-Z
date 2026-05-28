def missingnum(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

if __name__ == "__main__":
    nums = [3,0,1]
    result = missingnum(nums)
    print(result)