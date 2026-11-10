def solve():
    s = "babad"
    longest = ""

    for i in range(len(s)):
        for left, right in [(i, i), (i, i+1)]:

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if right - left + 1 > len(longest):
                    longest = s[left:right+1]

                left -= 1
                right += 1

    return longest
