def maxcountconsecutiveones(nums):
    max_count = 0
    current_count = 0
    for i in nums:
        if i==1:
            current_count +=1
        else:
            max_count = max(max_count,current_count)
            current_count = 0
    return max(max_count,current_count)

if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    result = maxcountconsecutiveones(nums)
    print(result)
