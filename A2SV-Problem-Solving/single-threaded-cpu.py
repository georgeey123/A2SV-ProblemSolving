class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enqueue_time, processing_time, i) for i, (enqueue_time, processing_time) in enumerate(tasks)]
        tasks.sort()

        n = len(tasks)
        result = []
        available_tasks = []

        time = 0
        i = 0

        while i < n or available_tasks:
            while i < n and tasks[i][0] <= time:
                enqueue_time, processing_time, index = tasks[i]
                heappush(available_tasks, (processing_time, index))
                i += 1

            if not available_tasks:
                time = tasks[i][0]
            else:
                processing_time, index = heappop(available_tasks)
                time += processing_time
                result.append(index)

        return result
