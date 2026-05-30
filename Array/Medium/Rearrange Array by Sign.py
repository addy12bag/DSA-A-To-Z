def rearrangeArray(nums):
    pos = []
    neg  = []
    for i in nums:
        if i>=0:
            pos.append(i)
        else:
            neg.append(i)
    
    postindx = 0
    negindx = 0

    i = 0
    while postindx<len(pos) and negindx<len(neg):
        if i%2 == 0:
            nums[i] = pos[postindx]
            postindx+=1
        else:
            nums[i] = neg[negindx]
            negindx +=1
        i +=1
    
    while postindx<len(pos):
        nums[i] = pos[postindx]
        postindx +=1
        i +=1
    while negindx<len(neg):
        nums[i] = neg[negindx]
        negindx +=1
        i +=1
    return nums


if __name__ == "__main__":
    nums = [3,1,-2,-5,2,-4]
    print(rearrangeArray(nums))



            