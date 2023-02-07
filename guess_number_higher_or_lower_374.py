def guessNumber(self, n):
        l, r = 1, n
        # while l <= r:
        #     mid = (l + r) // 2
        #     if guess(mid) == 0:
        #         return mid
        #     if guess(mid) < 0:
        #         r = mid - 1
        #     else:
        #         l = mid + 1