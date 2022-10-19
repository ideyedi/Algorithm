#! python
from typing import List


class Solution:
    """
    입력된 두 리스트를 오름차순으로 정렬하면서 합한다.
    입력된 리스트는 이미 정렬되어 있다.
    합쳐진 리스트의 중간 값(Median)을 구한다.
    - 리스트의 길이가 짝수일 경우 가운데 두 수의 평균
    - 리스트의 길이가 홀수일 경우 가운데 값
    Time complexity 'O(n+m)'
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length_1 = len(nums1)
        length_2 = len(nums2)
        ret = []
        # median, index1, index2
        m, i, j = 0, 0, 0

        # pivot이 따로 설정되어야..?
        while i < length_1 and j < length_2:
            if nums1[i] < nums2[j]:
                ret.append(nums1[i])
                i += 1
            else:
                ret.append(nums2[j])
                j += 1

        ret.extend(nums2[j:]) if j < length_2 else ret.extend(nums1[i:])
        m_index = len(ret) // 2
        if len(ret) % 2 == 1:
            m = ret[m_index]
        else:
            m = (ret[m_index] + ret[m_index - 1]) / 2

        return m


if __name__ == "__main__":
    num1 = [1, 2]
    num2 = [3]
    solution = Solution()
    ret = solution.findMedianSortedArrays(num1, num2)
    print(f'Output: {ret}')

