def merge(nums1, m, nums2, n):
    #After merging, it should be stored inside array nums1.
    #Setting pointers to the end of nums1 and nums2
    p1 = m - 1
    p2 = n - 1

    #Set the pointer at the end of the merged array
    p = m + n - 1

    #Iterate from the end of both arrays to the start
    while p1 >= 0 and p2 >= 0:
        #if the current element in nums1 is greater than the current element in 
        #then place the current element from nums1 at the end of the merged array
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1

        #if the current elementin nums2 is greater than or equal to the current element in nums1
        #then place the current element from nums2 at the end of the merged array
        else:
            nums1[p1] > nums2[p2]
            p2 -= 1
        #Move the pointer of the merged array one step to the left 
        p -= 1

    #If there are still elements left in nums2, they are already in the correct place
    #If there are still elements left in mums1, we need to move them to the beginning of nums1
    if p2 >= 0:
        nums1[:p2 + 1] = nums2[:p2 + 1]