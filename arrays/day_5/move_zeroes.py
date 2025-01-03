class MoveZeroes:

    def __init__(self, nums):
        self.nums = nums

    def move_zeroes(self):
        l, r = 0, 0
        while r < len(self.nums):
            if self.nums[r] != 0:
                self.nums[l], self.nums[r] = self.nums[r], self.nums[l]
                l += 1
            r += 1
        return self.nums


if __name__ == '__main__':
    move_zeroes = MoveZeroes([0, 1, 0, 3, 12])
    print(move_zeroes.move_zeroes())
