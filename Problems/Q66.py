# Q66 Plus One

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # num = digits[-1]
        # if num != 9:
        #     digits[-1] += 1
        # else:
        #     count = 0
        #     while num == 9 and len(digits) > 0:
        #         num = digits.pop(-1)
        #         count += 1
        #     if num == 9:
        #         digits.append(1)
        #         digits.append(0)
        #     else:
        #         digits.append(num + 1)
        #     while count > 1:
        #         digits.append(0)
        #         count -= 1
        # return digits
            
        strs = ''
        for i in digits:
            strs += str(i)
        num = int(strs) + 1
        return [int(i) for i in str(num)]
