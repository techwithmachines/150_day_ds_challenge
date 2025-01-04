class RunningSum:

    def __init__(self, nums):
        self.nums = nums

    def find_sum(self):
        for i in range(len(nums)):
            if i <= 0:
                continue
            self.nums[i] = self.nums[i] + self.nums[i-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    running_sum = RunningSum(nums)
    running_sum.find_sum()
    print(nums)
