from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result_str = ""
        i : int = 0

        while(True):
            if len(word1) == i:
                result_str += word2[i:]
                break
            elif len(word2) == i:
                result_str += word1[i:]
                break
            else:
                result_str += word1[i] + word2[i]
            i += 1

        return result_str


if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("ab", "qwe"))