def minWindow(source, target):
    # write your code here
    if source == '' or target == '':
        return ''

    dtest = {}
    for ch in set(target): dtest[ch] = 0

    dT = dict.copy(dtest)
    for ch in target: dT[ch] = dT[ch] + 1

    n = len(source)
    left = right = 0
    length = 0
    ans = ''

    while right < n:
        chrr = source[right]
        if chrr in dT:
            if dtest[chrr] < dT[chrr]:
                length += 1
            dtest[chrr] += 1
        if length == len(target):
            chrl = source[left]
            while left < right:
                if source[left] in dT:
                    if dtest[chrl] == dT[chrl]:
                        break
                    dtest[chrl] -= 1
                left += 1
                chrl = source[left]
            if ans == '' or right - left < len(ans):
                ans = source[left:right + 1]
            dtest[chrl] -= 1
            left += 1
            length -= 1
        right += 1
    return ans