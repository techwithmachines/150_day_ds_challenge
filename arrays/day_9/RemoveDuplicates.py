class RemoveDuplicates:

    def __init__(self, nums):
        self.nums = nums

    def remove_duplicates(self):
        l = 1
        for r in range(1, len(self.nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l


if __name__ == '__main__':
    nums = [1, 1, 2]
    remove_duplicates = RemoveDuplicates(nums)
    l = remove_duplicates.remove_duplcates()
    print(nums[:l])
