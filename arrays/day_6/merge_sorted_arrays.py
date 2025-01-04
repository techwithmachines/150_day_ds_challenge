class MergeSortedArrays:

    def __init__(self, nums1, nums2, m, n):
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = m
        self.n = n

    def merge(self):
        p1 = self.m - 1
        p2 = self.n - 1
        i = self.m + self.n - 1
        while p1 >= 0 and p2 >= 0:
            if self.nums1[p1] >= self.nums2[p2]:
                self.nums1[i] = self.nums1[p1]
                p1 -= 1
            else:
                self.nums1[i] = self.nums2[p2]
                p2 -= 1
            i -= 1

        while p2 >= 0:
            self.nums1[i] = self.nums2[p2]
            p2 -= 1
            i -= 1


if __name__ == '__main__':
    nums1 = [3, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 2]
    merge_sorted_array = MergeSortedArrays(nums1, nums2, 3, 3)
    merge_sorted_array.merge()
    print(nums1)
