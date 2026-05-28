def union_two_sorted_array(nums1,nums2):
    i = j =0
    union = []
    while i<len(nums1) and j<len(nums2):
        if nums1[i] < nums2[j]:
            union.append(nums1[i])
            i +=1
        elif nums1[i]>nums2[j]:
            union.append(nums2[j])
            j +=1
        else:
            union.append(nums1[i])
            i +=1
            j +=1
    union.extend(nums1[i:])       
    union.extend(nums2[j:])       
    return union

if __name__ == "__main__":
    nums1 = [1, 2, 4, 5, 6]
    nums2 = [2, 3, 5, 7]
    print(union_two_sorted_array(nums1,nums2))