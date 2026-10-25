class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        mod = 1337
        res = 1

        for dig in b:
            res = (pow(res, 10, mod) * pow(a, dig, mod)) % mod

        return res