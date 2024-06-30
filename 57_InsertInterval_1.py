class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start,end = newInterval[0],newInterval[1]
        left_arr = []
        right_arr = []

        for interval in intervals:
            if interval[1] < start:
                left_arr.append(interval)
            elif end < interval[0]:
                right_arr.append(interval)
            else:
                start = min(interval[0],start)
                end = max(interval[1],end)

        # arr = []
        # for interval in left_arr:
        #     arr.append(interval)
        # arr.append([start,end])
        # for interval in right_arr:
        #     arr.append(interval)

        return left_arr+[[start,end]]+right_arr