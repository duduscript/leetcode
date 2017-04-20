import Queue
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return []
        p,rtn = Queue.PriorityQueue(),[]
        for building in buildings:
            p.put(building)
        head = p.get()
        while p.qsize():
            building = p.get()
            if building[0] >= head[1]:
                if building[0] == head[1] and building[2] == head[2]:
                    head[1] = max(building[1],head[1])
                else:
                    rtn.append([head[0],head[2]])
                    if building[0] != head[1]:
                        rtn.append([head[1],0])
                    head = building
                continue
            if building[2] > head[2]:
                if building[0] != head[0]:
                    rtn.append([head[0],head[2]])
                if building[1] < head[1]:
                    p.put([building[1],head[1],head[2]])
                head = building
            elif building[2] == head[2]:
                head[1] = max(head[1],building[1])
            if building[2] < head[2] and building[1] > head[1]:
                p.put([head[1],building[1],building[2]])
        rtn.append([head[0],head[2]])
        rtn.append([head[1],0])
        return rtn