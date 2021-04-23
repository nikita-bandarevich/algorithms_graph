import utils
from collections import defaultdict
class Solution(object):
    def leastNumBus(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target: return 0
        routes, n = [set(r) for r in routes], len(routes)
        g = [set() for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if set(routes[i]) & set(routes[j]): 
                    g[i].add(j), g[j].add(i)
        visited = set(i for i,r in enumerate(routes) if source in r)
        destination = set(i for i,r in enumerate(routes) if target in r)
        q = [(x, 1) for x in visited]
        for x, d in q:
            if x in destination: return d
            for y in g[x]:
                if y not in visited: visited.add(y), q.append((y, d+1))
        return -1



if __name__ == '__main__':
    utils.score()
