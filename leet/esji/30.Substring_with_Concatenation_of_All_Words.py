from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 반환 값 리스트
        indices = []
        word_count = {}
        # word length는 모두 같다고 가정하고 있다.
        word_length = len(words[0])
        words_len = len(words)
        # 서브 스트링의 총 길이
        word_array_length = word_length * words_len

        # 's' null check input value
        # 'words' null check condition list
        # 조건, 입력 값이 null이면 반환 값을 null로 설정한다.
        if s is None or len(s) == 0 or words is None or words_len == 0:
            return indices

        # 해당하는 word가 문자열 안에 있을 경우 count 딕셔너리에 추가, key는 word 자체
        # 값이 없을 경우 1로 설정
        for i in range(words_len):
            if words[i] in word_count:
                word_count[words[i]] += 1
            else:
                word_count[words[i]] = 1

        for i in range(0, len(s) - word_array_length + 1):
            current = s[i:i + word_array_length]

            word_map = {}

            # index: Index to loop through the array
            # j: Index to partition the current string
            index, j = 0, 0

            while index < words_len:
                part = current[j: j + word_length]

                if part in word_map:
                    word_map[part] += 1
                else:
                    word_map[part] = 1

                j += word_length
                index += 1

            if word_map == word_count:
                indices.append(i)

        return indices


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    obj = Solution()

    print(obj.findSubstring(s, words))

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    obj = Solution()

    print(obj.findSubstring(s, words))

    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    obj = Solution()

    print(obj.findSubstring(s, words))

