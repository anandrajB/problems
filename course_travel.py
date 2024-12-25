from collections import defaultdict, deque
from typing import List

## using BFS


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # step1 initialize a graph and compute in_degreee
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        processed_item = 0

        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        # step2 add the queue

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # step 3 process the queue
        while queue:
            course = queue.popleft()
            processed_item += 1

            for neighbour_items in graph[course]:
                in_degree[neighbour_items] -= 1
                if in_degree[neighbour_items] == 0:
                    queue.append(neighbour_items)

        return processed_item == numCourses


# Example usage
numCourses = 2
prerequisites = [[1, 0]]
solution = Solution()
print(solution.canFinish(numCourses, prerequisites))  # Output: True
