import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']
        left_far, left_near, front, right_near, right_far = lidar



        left = (left_far + left_near) / 2
        right = (right_near + right_far) / 2
        width = left + right

        offset = (right - left) / max(width, 0.01)
        curve_signal = (right_far + right_near - left_far - left_near) / max(left_far + left_near + right_far + right_near, 0.01)

        steer = 3.0 * offset + 1.5 * curve_signal
        if steer > 0.05:
            steering = 'right'
        elif steer < -0.05:
            steering = 'left'
        else:
            steering = 'straight'

        target = 0.1 + 0.2 * min(front, width)
        target = min(target, 0.20)

        if abs(curve_signal) > 0.3:
            target = min(target, 0.2)
        if front < 0.5:
            target = min(target, 0.15)
        if abs(offset) > 0.7 or front < 0.3:
            target = min(target, 0.1)

        if velocity < target - 0.05:
            action = 'accelerate'
        elif velocity > target + 0.05:
            action = 'brake'
        else:
            action = 'coast'

        return (steering, action)