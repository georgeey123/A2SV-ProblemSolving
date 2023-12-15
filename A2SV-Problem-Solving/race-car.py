from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        start = (0, 0, 1)
        queue = deque([start])

        visited = set()
        visited.add(start)
        memo = {}

        while queue:
            moves, position, speed = queue.popleft()

            if position == target:
                return moves


            if (position, speed) in visited:
                continue
            else:
                visited.add((position, speed))
                queue.append((moves+1, position+speed, speed*2))

                if (position+speed > target and speed > 0) or (position+speed < target and speed < 0):
                    speed = -1 if speed > 0 else 1
                    queue.append((moves+1, position, speed))

            # new_pos = position + speed
            # new_speed = speed * 2
            # new_state = (moves + 1, new_pos, new_speed)

            # if new_state not in visited:
            #     visited.add(new_state)
            #     queue.append(new_state)

            # new_speed = -1 if speed > 0 else 1
            # new_state = (moves + 1, position, new_speed)

            # if new_state not in visited:
            #     visited.add(new_state)
            #     queue.append(new_state)

        return 0
