class MajorityElement:

    def __init__(self, nums):
        self.nums = nums

    def find_majority_element(self):
        majority_element = 0
        counter = 0
        for i in range(0, len(self.nums)):
            if counter == 0:
                majority_element = self.nums[i]
            counter += 1 if self.nums[i] == majority_element else -1
        return majority_element


if __name__ == '__main__':
    majority_element = MajorityElement([2, 2, 1, 1, 1, 2, 2])
    print(majority_element.find_majority_element())
