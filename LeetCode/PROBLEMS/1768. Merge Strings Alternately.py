class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        lst1 = list(word1)
        lst2 = list(word2)
        mList = []
        if n < m:
            c = 0
            indexes = [num for num in range(1, len(lst1) * 2 + 1, 2)]
            for i in range(len(lst1)):
                c += 1
                lst1.insert(i + c, 0)
            replacements = lst2
            for (index, replacement) in zip(indexes, replacements):
                lst1[index] = replacement

            lst2 = list(word2[c:])
            for i in range(len(lst2)):
                lst1.append(lst2[i])
            for a in lst1:
                mList.append(a)

        elif n > m:
            c = 0
            indexes = [num for num in range(1, len(lst2) * 2 + 1, 2)]
            for i in range(len(lst2)):
                c += 1
                lst1.insert(i + c, 0)
            replacements = lst2
            for (index, replacement) in zip(indexes, replacements):
                lst1[index] = replacement
            for a in lst1:
                mList.append(a)

        elif n == m:
            for i in range(len(lst1)):
                mList.append(lst1[i])
                mList.append(lst2[i])

        merged = str(''.join(mList))
        return merged


ans = Solution()
ans.mergeAlternately("abccc", "pqrs")
