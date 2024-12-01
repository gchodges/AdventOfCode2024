import heapq
from collections import Counter

def part1(nums1, nums2):
    heapq.heapify(nums1)
    heapq.heapify(nums2)
    res = 0

    while nums1:
        num1 = heapq.heappop(nums1)
        num2 = heapq.heappop(nums2)

        res += abs(num1 - num2)

    return res

def part2(nums1, nums2):
    res = 0

    appearances = Counter(nums2)
    for n in nums1:
        res += n * appearances.get(n, 0)

    return res
        

if __name__ == "__main__":
    with open('./input.txt', 'r') as input:
        nums1 = []
        nums2 = []
        for line in input:
            nums = line.split('   ')
            nums1.append(int(nums[0]))
            nums2.append(int(nums[1].strip()))

        print(part1(nums1[::], nums2[::]))
        print(part2(nums1[::], nums2[::]))