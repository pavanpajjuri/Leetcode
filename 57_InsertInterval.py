class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        merged_interval = intervals[0]

        for start,end in intervals[1:]:
            if start > merged_interval[-1][1]:
                merged_interval.append([start,end])
            else:
                merged_interval[-1] = [merged_interval[-1][0],max(merged_interval[-1][1],end)]
        
        return merged_interval