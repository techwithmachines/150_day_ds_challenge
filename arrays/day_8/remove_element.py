class RemoveElement:

    def __init__(self, nums, x):
        self.nums = nums
        self.x = x

    def remove(self):
        l = 0
        for r in range(0, len(self.nums)):
            if self.nums[r] != self.x:
                self.nums[l] = self.nums[r]
                l += 1
        return l


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    x = 3
    remove_element = RemoveElement(nums, x)
    l = remove_element.remove()
    print(nums[:l])