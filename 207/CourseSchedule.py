class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        oldnum,pre,aft,table = numCourses,{},{},[1]*numCourses
        for i in xrange(numCourses):
            pre[i],aft[i] = set(),set()
        for pair in prerequisites:
            pre[pair[1]].add(pair[0])
            aft[pair[0]].add(pair[1])
        while numCourses:
            for course_num in pre:
                if table[course_num] == 0:
                    continue
                if len(pre[course_num]) == 0:
                    numCourses -= 1
                    table[course_num] = 0
                    for course_aft in aft[course_num]:
                        if course_num in pre[course_aft]:
                            pre[course_aft].remove(course_num)
            if numCourses == oldnum:
                return False
            else:
                oldnum = numCourses
        return True