# Q848 Shifting Letters

# We have a string S of lowercase letters, and an integer array shifts.

# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

# Return the final string after all such shifts to S are applied.

# Example 1:

# Input: S = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: 
# We start with "abc".
# After shifting the first 1 letters of S by 3, we have "dbc".
# After shifting the first 2 letters of S by 5, we have "igc".
# After shifting the first 3 letters of S by 9, we have "rpl", the answer.
# Note:

# 1 <= S.length = shifts.length <= 20000
# 0 <= shifts[i] <= 10 ^ 9


class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        S = [i for i in S]
        for val in range(len(shifts)):
            shifts[val] = shifts[val] % 26
        
        maximum = sum(shifts)
        for val in range(len(shifts)):
            ind = ord(S[val]) + maximum
            S[val] = chr((ind - 97) % 26 + 97)
            maximum -= shifts[val]
            
        
        ans = ''
        for i in S:
            ans += i
        return ans
                
        
        
#         S = [i for i in S]
#         for i in range(len(shifts)):
#             for ch in range(len(S[0:i + 1])):
#                 ind = ord(S[ch]) + shifts[i]
#                 S[ch] = chr((ord(S[ch]) + shifts[i] - 97) % 26 + 97)
#         ans = ''
#         for i in S:
#             ans += i
#         return ans
        
        

            
        