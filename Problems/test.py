# Input: 
# S = "abcdebdde", T = "bde"
# Output: "bcde"


def test(S, T):
    """
    :type S: str
    :type T: str
    :rtype: str
    """


    if S == '' or T == '':
        return ''
    ans = ''
    n = len(S)
    m = len(T)
    window = n
    left = right = 0
    while left < n:
        letter = T[0]
        select = 1
        if S[left] == letter:
            right = left + 1
            while right < n:
                while select < m:
                    if S[right] == T[select]:
                        select += 1
                        print select
                    right += 1
            if right - left < window:
                ans = S[left:right]
        left = right + 1
        print left, right
    return ans

