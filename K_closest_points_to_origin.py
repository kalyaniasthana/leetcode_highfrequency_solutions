"""
I clicked on the 'Related Topics' tab under the question description,
saw 'HEAP' and instantly knew what to do.
I knew how to use the heapq python library to implement a minheap
priority queue already...since I used that for my AI class project 

However....
Later when I saw the solution after submitting mine, I realised I could have used a lambda
function embedded in the sort function haha... so easy.

Do they ask how to implement heaps or sorting algorithms (merge, heap, quick) from 
scratch during coding interview? oh man, I really hope they don't. 
Who the fuck remembers that shit? 
"""

import heapq
import math

class MyHeap:
    def  __init__(self):
        self.Heap = []
        
    def push(self, point, dist_to_origin):
        entry = (dist_to_origin, point)
        heapq.heappush(self.Heap, entry)
        
    def pop(self):
        (_, point) = heapq.heappop(self.Heap) 
        return point
        
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def dist_calculator(point1, point2):
            dist = math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
            return dist
        
        heap = MyHeap()
        origin = [0, 0]
        for point in points:
            # entry = (point, dist_calculator(point, origin))
            # print(entry)
            if point[0] > -10000 and point[0] < 10000 and point[1] > -10000 and point[1] < 10000:
                heap.push(point, dist_calculator(point, origin))
        points = []
        for i in range(K):
            points.append(heap.pop())
        return points