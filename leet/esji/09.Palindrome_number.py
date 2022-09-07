class Solution:
    def __init__(self):
        pass

    def isPalindrome(self, x: int) -> bool:
        # int x가 0보다 작은 경우 회문조건에 성립하지 않는다
        if x < 0:
            return False
        str_x = str(x)
        length = len(str(x))
        loop = length // 2
        index = 0

        while loop > index:
            #print(f'{str_x[index]}')
            #print(f'{str_x[length - index - 1]}')
            if str_x[index] != str_x[length - index - 1]:
                return False

            index += 1

        return True


if __name__ == "__main__":
    x = 121

    ins_solution = Solution()
    ret = ins_solution.isPalindrome(x)
    print(f'{ret}')
