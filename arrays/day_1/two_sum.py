class TwoSum:

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_pair(self):
        res = []
        count = {}
        for i,n in enumerate(self.nums):
            diff = self.target - n
            if diff in count:
                res = [count.get(diff), i]
                return res
            count[n] = i
        return res


if __name__ == '__main__':
    two_sum = TwoSum([3, 6, 2, 4], 5)
    print(two_sum.find_pair())
