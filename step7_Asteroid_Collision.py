'''find the asteroid collision
example:
input: [5, 10, -5]
output: [5, 10]
explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
'''
def asteroidCollision(asteroids):
    stack = [] # store asteroids that are still moving
    for asteroid in asteroids: # take every asteroid
       while stack and asteroid < 0 < stack[-1]: # check if current asteroid is moving left and top of stack is moving right
            if stack[-1] < -asteroid: # if top of stack is smaller than current asteroid
                stack.pop() # remove top of stack
                continue # continue checking with next asteroid in stack
            elif stack[-1] == -asteroid: # if top of stack is equal to current asteroid
                stack.pop() # remove top of stack
            break # if top of stack is larger than current asteroid, current asteroid is destroyed, so break out of loop
    else:
        stack.append(asteroid) # add current asteroid to stack if it doesn't collide
    return stack
asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))
'''tc: O(n) because each asteroid is pushed and popped at most once
sc: O(n) because in worst case all asteroids are in stack (e.g. all moving in same direction)
'''