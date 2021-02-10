""" O(n) solution. thank you again to Nick White's videos.
He didn't take this case into account though: when the next
interval is inside the current interval -> need to check
min of curr_begin and next_begin for this case.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # are the intervals necessarily sorted? NO. 
        # right then use sort and merge
        
        if len(intervals) == 1: #if there is only one interval
            return intervals
        intervals.sort() # python sorts according to first element
        # of each interval by default
        curr_int = intervals[0] # current interval
        output_array = [curr_int] #initialise output array with current/first interva;
        i = 0 # pointer to current interval in output array
        for interval in intervals:
            curr_begin, curr_end = curr_int[0], curr_int[1]
            next_begin, next_end = interval[0], interval[1]
            if curr_end >= next_begin:
                output_array[i][0] = min(curr_begin, next_begin) # don't forget to check this too, vv imp
                # ^ the above line is for when the next interval is inside the current interval
                output_array[i][1] = max(curr_end, next_end)
            else:
                curr_int = interval # if there is no merge then add next interval to output array
                # and update pointer to current interval
                output_array.append(curr_int)
                i += 1
        return output_array
        