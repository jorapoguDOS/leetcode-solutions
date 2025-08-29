class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        # Fast Runtime
        return [sum(math.sqrt((x0 - x1)**2 + (y0 - y1)**2) <= r for x0,y0 in points) for x1,y1,r in queries]
        
        # def dist(x,y):
        #     return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

        # iterate queries first
        # ans = []
        # for j in queries:
        #     p = sum(dist(i,j) <= j[2] for i in points)
        #     ans.append(p)
        # return ans

        # # Iterate points fist
        # ans = [0 for _ in range(len(queries))]
        # for i in points:
        #     for j in range(len(queries)):
        #         if dist(i,queries[j]) <= queries[j][2]:
        #             ans[j] += 1
        # return ans
        

