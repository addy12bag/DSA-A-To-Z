def majorityelement(nums):
    if not nums:
        return None
    count1 = count2 = 0
    candidate1 = candidate2 = None

    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    
    result = []
    for candidate in [candidate1, candidate2]:
        if nums.count(candidate) > len(nums) // 3:
            result.append(candidate)
    return result


if __name__ == "__main__":
    nums = [1,2]
    print(majorityelement(nums))