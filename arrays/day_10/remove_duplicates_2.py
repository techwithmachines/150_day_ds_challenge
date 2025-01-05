class RemoveDuplicatesTwo:

    def __init__(self, nums):
        self.nums = nums

    def remove_duplicates(self):
        l, r = 0, 0
        while r < len(self.nums):
            count = 1
            while r + 1 < len(self.nums) and self.nums[r] == self.nums[r + 1]:
                count += 1
                r += 1
            count = min(count, 2)
            for i in range(count):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 3, 3]
    remove_duplicates = RemoveDuplicatesTwo(nums)
    print("input : " + str(nums))
    l = remove_duplicates.remove_duplicates()
    print("output : " + str(nums[:l]))
