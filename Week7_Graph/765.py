from typing import List
import collections


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        d = collections.defaultdict(list)
        for i, ele in enumerate(row):
            d[ele//2].append(i)
        swap = 0
        for odd in range(0, len(row), 2):
            even = odd + 1
            num_odd = row[odd]
            num_even = row[even]
            if even in d[num_odd//2]:
                continue
            else:
                #print(odd, num_odd, even, num_even)
                swap_place = d[num_odd//2][0] if d[num_odd//2][0] != odd else d[num_odd//2][1]
                row[even], row[swap_place] = row[swap_place], row[even]
                d[num_even//2][d[num_even//2].index(even)] = swap_place
                swap += 1
        #print(d)
        return swap