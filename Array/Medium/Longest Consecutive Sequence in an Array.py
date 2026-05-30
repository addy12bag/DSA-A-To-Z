def Longest_consecutive_sequence(nums):
    if not nums:
        return None
    num_set = set(nums)
    longest_streak = 1
    current_streak = 1
    for num in num_set:
        if num-1 not in num_set:
            current_num = num
            
            while current_num+1 in num_set:
                current_num +=1
                current_streak +=1

    return max(longest_streak,current_streak)

if __name__ =="__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(Longest_consecutive_sequence(nums))

    nums = [0, -1, 1, 2, -2]
    print(Longest_consecutive_sequence(nums))  

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(Longest_consecutive_sequence(nums))  
