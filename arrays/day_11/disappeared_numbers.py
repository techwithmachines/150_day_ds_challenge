class DisappearedNumbers:

    def __init__(self, nums):
        self.nums = nums

    def disappear_nums(self):
        res = []
        for i in range(len(self.nums)):
            pos = abs(self.nums[i]) - 1
            self.nums[pos] = -1 * abs(self.nums[i])
        for i in range(len(self.nums)):
            if self.nums[i] > 0:
                res.append(i+1)
        return res


if __name__ == '__main__':
    nums = [1, 4, 4, 4]
    disappeared_nums = DisappearedNumbers(nums)
    print(disappeared_nums.disappear_nums())
