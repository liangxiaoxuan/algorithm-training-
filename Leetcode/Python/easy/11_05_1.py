# 3.Remove Element
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,3,0,0], your answer will be accepted.


def remove_element(nums,val):
    n = 0
    for i in nums:
        if i == val:
            del nums[n]
        n += 1
    print(len(nums))


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    val = 5
    remove_element(nums, val)