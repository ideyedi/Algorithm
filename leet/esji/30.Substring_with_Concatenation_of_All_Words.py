from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        word_count = len(words)

        return 0


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    obj = Solution()

    print(obj.findSubstring(s, words))

