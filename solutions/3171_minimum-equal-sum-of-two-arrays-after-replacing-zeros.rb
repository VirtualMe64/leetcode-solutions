# Problem: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros
# Runtime: 139 ms

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_sum(nums1, nums2)
    # step 1: get neccesary values
    sum1, sum2 = nums1.sum, nums2.sum
    zeros1, zeros2 = nums1.count(0), nums2.count(0)

    # 0s must become strictly positive, so smallest possible sum is sum + # of zeros
    min_sum1 = sum1 + zeros1
    min_sum2 = sum2 + zeros2

    # if we don't have zeros and need to increase, impossible
    return -1 if (zeros1 == 0 && min_sum1 < min_sum2) || (zeros2 == 0 && min_sum2 < min_sum1)

    return [min_sum1, min_sum2].max
end