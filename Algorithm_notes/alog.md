### Kadane's algorithm
*So we assume that the largest subarray is the first element, then we go through A[1:] elements (all elements except the first one).
Kadane算法的执行流程，从头到尾遍历目标数组，将数组分割为满足上述条件的子串，同时得到各子串的最大前缀和，然后比较各子串的最大前缀和，得到最终答案。我们以array={−2, 1, −3, 4, −1, 2, 1, −5, 4}为例，来简单说明一下算法步骤。通过遍历，可以将数组分割为如下3个子串（-2），（1，-3），（4，-1，2，1，-5，4），这里对于（-2）这样的情况，单独分为一组。各子串的最大前缀和为-2，1，6，所以目标串的最大子串和为6