# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary)
# You may assume that the intervals were initially sorted according to their start times.

class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        # Adding new interval into intervals
        intervals.append(newInterval)
        # Sorting intervals
        intervals = sorted(intervals)
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current interval does not overlap 
            # with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

sol = Solution()
print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
