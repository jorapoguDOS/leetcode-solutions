class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        maxim_change = [(
            - ( ((x+1)/(y+1)) - (x/y) ), 
            x, 
            y)
            for x, y in classes]
        heapq.heapify(maxim_change)

        for _ in range(extraStudents):
            change, x, y = heapq.heappop(maxim_change)
            heapq.heappush( maxim_change,(
                - ( ((x+2)/(y+2)) - ((x+1)/(y+1)) ),
                x + 1,
                y + 1
            ))

        total_pass_r = sum(x/y for _, x, y in maxim_change)

        return total_pass_r / len(classes)

        