def uniquenumber(nums):
    result = 0
    for num in nums:
        num = num ^ result
        result = num
    return result

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    result = uniquenumber(nums)
    print(result)