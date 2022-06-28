#question link:https://leetcode.com/problems/asteroid-collision/
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                collision_ended = False
                while stack and (stack[-1] >= 0 and asteroid < 0) and not collision_ended:
                    old = stack.pop()
                    if old + asteroid >= 0:
                        collision_ended = True
                    if old + asteroid > 0:
                        stack.append(old)
                if not collision_ended:
                    stack.append(asteroid)
        return stack


#question link:https://leetcode.com/problems/count-collisions-on-a-road/
class Solution:
    def countCollisions(self, directions: str) -> int:
        score = 0
        for i in directions.lstrip('L').rstrip('R'):
            if i != 'S':
                score += 1
        return score

