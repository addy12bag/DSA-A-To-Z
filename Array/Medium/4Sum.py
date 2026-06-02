def sum_four(nums,target):
    res_set =set()
    n = len(nums)

    for i in range(n):
        for j in range(i+1,n):
            s = set()
            for k in range(j+1,n):
                sum_val = nums[i]+nums[j]+nums[k]

                last = target-sum_val
                if last in s:
                    curr = sorted([nums[i], nums[j], nums[k], last])
                    res_set.add(tuple(curr))
                s.add(nums[k])
    return [list(t) for t in res_set]

if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(sum_four(nums,target))