# Q14 Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if strs == []:
        #     return ''
        # if strs[0] == "":
        #     return ''
        # if len(strs) == 1:
        #     return strs[0]
        # ans = ''
        # count = 0
        # while count < len(strs[0]):
        #     lst = []
        #     for word in strs:
        #         if len(word) < count + 1:
        #             return ans
        #         else:
        #             lst.append(word[count])
        #     if len(set(lst)) == 1:
        #         ans += lst[0]
        #         count += 1
        #     else:
        #         break
        # return ans
        
        if strs == None or strs == []:
            return ''
        prefix = strs[0]
        for i in strs[1:]:
            while i.find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                if len(prefix) == 0:
                    return ''
        return prefix
