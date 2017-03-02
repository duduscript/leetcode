class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        path,courses = [],set(range(numCourses))
        while len(courses):
            noprecourse = courses - set(map(lambda req:req[0],prerequisites))
            if len(noprecourse) == 0:
                return []
            path += list(noprecourse)
            courses = courses - noprecourse
            prerequisites = filter(lambda req:req[1] not in noprecourse,prerequisites)
        return path