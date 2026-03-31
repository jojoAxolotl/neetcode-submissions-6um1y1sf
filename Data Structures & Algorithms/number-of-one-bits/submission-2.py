class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # 如果最後一位是 1，count 就加 1
            n >>= 1         # 數字向右移一位
        return count