class SquaresSortedArray:

    def __init__(self, nums):
        self.nums = nums

    def find_squares(self):
        l, r = 0, len(self.nums) - 1
        output = [0] * len(self.nums)
        i = len(self.nums) - 1
        while l <= r:
            left = abs(self.nums[l])
            right = abs(self.nums[r])
            if left >= right:
                output[i] = left ** 2
                l += 1
            else:
                output[i] = right ** 2
                r -= 1
            i -= 1
        return output


if __name__ == '__main__':
    squares_sorted_array = SquaresSortedArray([-4, -1, 0, 3, 10])
    print(squares_sorted_array.find_squares())
